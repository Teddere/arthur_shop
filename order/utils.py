import uuid

def _generate_ref():
    return str(uuid.uuid4()).upper()[:12]