from django.contrib import admin
from Psychbudapp.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['Name','MobileNo','Email','Password']
admin.site.register(User,UserAdmin)
