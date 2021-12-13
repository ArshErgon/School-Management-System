from django.contrib import admin

# Register your models here.
from .models import UserRegistion

class UserAdmin(admin.ModelAdmin):
    list_display = ('Fname','insitution', 'city', 'phone_number')


admin.site.register(UserRegistion, UserAdmin)