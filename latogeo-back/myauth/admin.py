from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from myauth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.forms import AdminPasswordChangeForm
from myauth.models import MyUser
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.admin import TokenAdmin
# Register your models here.

class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    readonly_fields = ('confirmation_key',)
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'ra', 'first_name', 'last_name', 'is_staff',
                    'is_active', 'terms', 'level')
    list_filter = ('is_active', 'is_staff', 'terms', 'level')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'ra', 'confirmation_key')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Status', {'fields': (
            'is_staff', 'is_active', 'is_confirmed','terms', 'level')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser',
                                       'groups', 'user_permissions')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('email',)

TokenAdmin.raw_id_fields = ('user',)

# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)

