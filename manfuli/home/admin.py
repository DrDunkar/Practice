from django.contrib import admin
from home.models import user
from home.models import Address
# Register your models here.
admin.site.register(user)
admin.site.register(Address)