from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import Http404
from decimal import Decimal

import stripe

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import ProductItem
from .models import Order,OrderItem
from .serializers import OrderSerializer,MyOrderSerializer

User = get_user_model()

@api_view(['post'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])

def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        items = serializer.validated_data['items']
#      montant total recalculé
        paid_amount = Decimal('0')

        for item in items:
            Product_item = ProductItem.objects.get(id=item['productItem'])
            unit_price = Product_item.newPrice or Product_item.base_price
            paid_amount += unit_price * item['quantity']
        
        stripe.api_key = settings.STRIPE_SECKEY_KEY

        try:
            charge = stripe.Charge.create(
                amount = int(paid_amount * 100),
                currency='EUR',
                description='Achat sur Arthur Shop',
                source= serializer.validated_data['stripe_token'],
            )
        except Exception as e:
            return Response({'detail':str(e.user_message or e)}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = serializer.save(user=request.user,paid_amount=paid_amount)
        except Exception as e:
        # Le paiement est passé mais la commande n'a pas pu être créée.
        # stripe.Refund.create(charge=charge.id)
            return Response({'detail':str(e)},status=status.HTTP_400_BAD_REQUEST)

        return Response('Order validated')
    else:
        return Response({'detail': 'Informations invalidées !'},status=status.HTTP_400_BAD_REQUEST)

    
class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)

