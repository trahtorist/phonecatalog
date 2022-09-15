from django.contrib import admin
from gbwphone.models import PhoneCatalog


class PhoneCatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "manufacturer", "device_name", "device_model", "active")
    search_fields = ("manufacturer", "device_name")
    list_filter = ("manufacturer", "device_name", "active")


admin.site.register(PhoneCatalog,PhoneCatalogAdmin)
