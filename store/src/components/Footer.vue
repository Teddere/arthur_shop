<script setup>
import {ref} from 'vue'
const date = ref(new Date())
</script>

<template>
<!-- ======== NEWSLETTERS ======================== -->
  <section class="newsletter section">
      <div class="newsletter__container container grid">
        <h3 class="newsletter__title flex">
          <i class="fa-solid fa-envelope"></i>
          Inscrivez-vous à la newsletter
        </h3>
        <p class="newsletter__description">
          ... et recevez un coupon de 25 $ pour votre premier achat.
        </p>
        <form action="#" class="newsletter__form">
          <input type="text" name="newsletter" id="newsletter" placeholder="Entrez votre adresse email" class="newsletter__input">
          <button type="submit" class="newsletter__btn">S'inscrire</button>
        </form>
      </div>
    </section>
<!-- ======= FOOTER ============================ -->
  <section class="footer-section container">
    <div class="footer__container grid">
      <div class="footer__content">
        <a href="#" class="footer__logo">
          <img src="@/assets/images/logo.png" alt="website logo" class="footer__logo-img"/>
        </a>
        <h4 class="footer__subtitle">Contact</h4>
        <p class="footer__description">
          <span>Téléphone :</span> +33 03 21 30 10 40
        </p>
        <p class="footer__description">
          <span>Horaires :</span> 10:00 - 19:00, lundi - samedi
        </p>
        <div class="footer__social">
          <h4 class="footer__subtitle">Suivez-nous</h4>
          <div class="footer__social-links flex">
            <a href="#" class="footer__social-icon">
              <i class="fa-brands fa-facebook-f"></i>
            </a>
            <a href="#" class="footer__social-icon">
              <i class="fa-brands fa-tiktok"></i>
            </a>
            <a href="#" class="footer__social-icon">
              <i class="fa-brands fa-youtube"></i>
            </a>
          </div>
        </div>
      </div>
      <div class="footer__content">
        <h4 class="footer__title">A propos</h4>
        <ul>
          <li><a href="#" class="footer__link">A propos de nous</a></li>
          <li><a href="#" class="footer__link">Livraison</a></li>
          <li><a href="#" class="footer__link">Polique de confidentialité</a></li>
        </ul>
      </div>
      <div class="footer__content">
        <h3 class="footer__title">Compte</h3>
        <ul class="footer__links">
          <li><a href="#" class="footer__link">Connexion</a></li>
          <li><a href="#" class="footer__link">Panier</a></li>
          <li><a href="#" class="footer__link">Commande</a></li>
          <li><a href="#" class="footer__link">Aide</a></li>
        </ul>
      </div>
      <div class="footer__content">
        <h3 class="footer__title">Paiment sécursé</h3>
        <span class="fa-brands fa-cc-visa payment__img"></span>
        <span class="fa-brands fa-cc-paypal payment__img"></span>
        <span class="fa-brands fa-cc-apple-pay payment__img"></span>
        <span class="fa-brands fa-cc-amex payment__img"></span>
        <span class="fa-brands fa-cc-amazon-pay payment__img"></span>
      </div>
    </div>
    <div class="footer__bottom">
      <p class="copyright">&copy; {{date.getFullYear()}} | Tous droit réservé</p>
    </div>
  </section>
</template>


