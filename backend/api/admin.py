from django.contrib import admin

from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display= ['username', 'email']


class ProfileAdmin(admin.ModelAdmin):
    list_editable=['is_verified']
    list_display= ['full_name', 'user', 'is_verified']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)    