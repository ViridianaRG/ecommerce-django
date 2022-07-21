from django.contrib import admin

from accounts.models import Account
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    #se despliegan los detalles de los campos de los usuarios
    list_display =  ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')#propiedades que quiero que se muestren dentro de la tabla
    #cuando el usuario le de click a una particular columna este me linkee hacia los detalles del usuario
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(Account, AccountAdmin)
