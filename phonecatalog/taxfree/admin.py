from django.contrib import admin
from taxfree.models import Puesc
from .models import *


class PuescAdmin(admin.ModelAdmin):
    list_display = ("taxid", "puesc_answer")
    search_fields = ("taxid",)

admin.site.register(Puesc, PuescAdmin)
