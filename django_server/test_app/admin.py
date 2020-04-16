from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser

'''
FROM: USER APP
'''
class MyUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    #form = UserChangeForm
    #add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('user_id', 'username', 'first_name', 'last_name', 'email', 'last_access', 'creation_date', 'last_update')
    list_filter = ('user_type',)
    fieldsets = (
        (None, {'fields': ('user_id', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', )}),
        ('Permissions', {'fields': ('is_admin', 'is_staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('user_id', 'username', 'first_name', 'last_name', 'email',)
    ordering = ('username', 'last_access', 'creation_date', 'last_update')
    filter_horizontal = ()

admin.site.register(MyUser, MyUserAdmin)
