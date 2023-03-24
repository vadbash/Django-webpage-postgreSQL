from django.contrib import admin
from .models import UserList

class UserListAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'password', 'registration_date')


admin.site.register(UserList, UserListAdmin)