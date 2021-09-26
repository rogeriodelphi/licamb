from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('date_joined', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser')
    list_filter = ('username', 'first_name', 'email', 'is_staff', 'is_superuser')