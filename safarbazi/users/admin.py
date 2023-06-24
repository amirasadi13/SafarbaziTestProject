from django.contrib import admin

# Register your models here.
from safarbazi.users.models import BaseUser

admin.site.register(BaseUser)