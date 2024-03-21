from django.contrib import admin
from .models import User , Department

# Register your models here.

# to show the fileds in a table in admin panel
class UserAdmin(admin.ModelAdmin):
    list_display = ['username' , 'email' , 'address' , 'tall' , 'dep_id']


admin.site.register(User , UserAdmin)
admin.site.register(Department)