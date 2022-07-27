from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangForm, CustomUserCreateForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangForm
    model = CustomUser
    list_display = ['username', 'email', 'age']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)