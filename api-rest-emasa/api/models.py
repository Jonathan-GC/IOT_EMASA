#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
import binascii
import os

#User = get_user_model()
# models here.





class Tenant (models.Model):
    name = models.CharField(max_length=100, unique=True)
    chirpstack_id = models.CharField(max_length=36,blank=True, null=True)
    Can_have_gateways = models.BooleanField(default=False)
    private_gateways_up = models.BooleanField(default=False)
    private_gateways_down = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

class CustomUser(AbstractUser):
    
    email = models.EmailField(unique = True)
    chirpstack_id = models.CharField(max_length=36,blank=True, null=True)
    
    ROLE_CHOISES = [
        ("viewer", "solo visualizacion"),
        ("controller", "controlar la maquina"),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOISES, default="viewer")
    #groups = models.ManyToManyField("auth.Group", related_name ="custom_users",blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="customuser_set",  # Nombre único para la relación inversa
        related_query_name="customuser",
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",  # Nombre único para la relación inversa
        related_query_name="customuser",
    )

    def __str__(self):
        return self.username
    


class CentralSystem (models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if CentralSystem.objects.exists() and not self.pk:
            raise ValueError("Solo puede existir una central.")
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name


class Machine (models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="machines")#DUEÑO DE LA MAQUINA
    central = models.ForeignKey(CentralSystem, on_delete=models.CASCADE)
    is_on = models.BooleanField(default=False)
    predictivo = models.BooleanField(default=False)
    gps = models.JSONField(default=dict)

    def __str__(self):
        return self.name



class Registro(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    Fecha = models.DateField(auto_now_add=True)
    TimeStamp = models.DateTimeField(auto_now_add=True)
    Pressure = models.FloatField(default=0.0)
    Current = models.FloatField(default=0.0)
    Temperature = models.FloatField(default=0.0)
    Voltage = models.FloatField(default=0.0)

    def __str__(self):
        return f"Registro de {self.machine.name if self.machine else 'Sin máquina'} - {self.Fecha}"
    
    
    
    

class CustomToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # Usará api_customuser
        related_name='custom_tokens',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key