from django.contrib import admin
from pharma.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class PharmacieAndAccount_Inline(admin.StackedInline):
    model = PharmacieAndAccount
    can_delete = False
    verbose_name_plural = 'PharmacieAndAccounts'

class CustomizedUserAdmin(UserAdmin):
    inlines = (PharmacieAndAccount_Inline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

admin.site.register(PharmacieAndAccount)
admin.site.register(Produit)
admin.site.register(Stock)
