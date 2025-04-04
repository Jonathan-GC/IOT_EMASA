import os
import django
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from api.models import CentralSystem

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf.settings')  
django.setup()

User = get_user_model()

SUPERUSERS = [

{"username" : "EMASADOCK",
"email" : "admin@example.com",
"password" : "emasa123"},
{"username" : "Jemison00",
"email" : "Jadmin@example.com",
"password" : "2025jemisonM*"},
]

for user in SUPERUSERS:
 if not User.objects.filter(username=user["username"]).exists(): #&& Y EL OTRO
    User.objects.create_superuser(user["username"], user["email"], user["password"]) #&& Y EL OTRO
    print(f"Superusuario '{user['username']}' creado con éxito.")
 else:
    print("Superusuario {user['username']}' ya existe, no se creó uno nuevo.")




SITE_ID = 1
SITE_DOMAIN = "localhost:8000"
SITE_NAME = "Mi Sitio Local"

site, created = Site.objects.update_or_create(
    id=SITE_ID,
    defaults={"domain": SITE_DOMAIN, "name": SITE_NAME},
)

if created:
    print(f"✅ Sitio creado con ID {SITE_ID}, dominio {SITE_DOMAIN}")
else:
    print(f"✅ Sitio actualizado con ID {SITE_ID}, dominio {SITE_DOMAIN}")


CENTRAL_NAME = "EMASA"

if not CentralSystem.objects.filter(name=CENTRAL_NAME).exists():
    CentralSystem.objects.create(name=CENTRAL_NAME)
    print("La central se creò con èxito")
else:
    print("Ya existe una central")