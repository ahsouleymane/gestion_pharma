from django.contrib import admin
from pharma.models import PharmacieAndAccount
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class PharmacieAndAccount_Inline(admin.StackedInline):
    model = PharmacieAndAccount
    can_delete = False

class CustomizedUserAdmin (UserAdmin):
    inlines = (PharmacieAndAccount_Inline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
