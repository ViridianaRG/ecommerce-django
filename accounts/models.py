from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
#clase para crear usuarios
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('El usuario debe de tener un email')
        if not username:
            raise ValueError('El usuario debe de tener un username')

        #si tiene email u username procedera a crear el usuario
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        #para la clave
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True) #para que sea unico
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    #Campos atributos de django
    date_joined = models.DateTimeField(auto_now_add=True) #fecha de creacion del usuario
    last_login = models.DateTimeField(auto_now_add=True) #ultima vez que el usuario estuvo en linea
    is_admin = models.BooleanField(default=False) #para saber si es administrador
    is_staff = models.BooleanField(default=False) #para saber si es staff
    is_active = models.BooleanField(default=False) #para saber si esta activo
    is_superadmin = models.BooleanField(default=False) #para saber si es superadmin

    USERNAME_FIELD = 'email' #que el parametro del login sea el email
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] #datos requeridos obligatorios

    objects = MyAccountManager()

    def __str__(self): #en admin para que se registre un label
        return self.email

    def has_perm(self, perm, obj=None): #si tiene permiso de admin
        return self.is_admin
    
    def has_module_perms(self, add_label): #si es admin para que tenga permiso
        return True
