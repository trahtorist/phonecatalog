from django.contrib import admin
from gbwphone.models import PhoneCatalog


class GbwphoneAdmin(admin.ModelAdmin):
    list_display = ("id", "manufacturer", "device_name", "device_model", "active")
    search_fields = ("manufacturer", "device_name")
    list_filter = ("manufacturer", "device_name")


admin.site.register(PhoneCatalog, GbwphoneAdmin)
