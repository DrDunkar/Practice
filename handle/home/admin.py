from django.contrib import admin
from .models import department
from .models import Food_item,PhoneNum

class PhoneNumInline(admin.TabularInline):
    model =PhoneNum

class departmentadmin(admin.ModelAdmin):
    inlines = [PhoneNumInline]
    class Meta:
        model = department


admin.site.register(department,departmentadmin)
# admin.site.register(department)
admin.site.register(Food_item)
admin.site.register(PhoneNum)
