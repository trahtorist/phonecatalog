from django.contrib import admin
from gbwphone.models import PhoneCatalog


class gbwphoneAdmin(admin.ModelAdmin):
    list_dispay = ("id", "manufacturer", "device_name", "device_model", "active")
    search_fields = ("manufacturer","device_name")
    list_filter = ("manufacturer","device_name")

admin.site.register(PhoneCatalog, gbwphoneAdmin)
