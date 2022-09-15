from django.contrib import admin
from taxfree.models import Puesc
from .models import *


class PuescAdmin(admin.ModelAdmin):
    list_display = ("taxid", "puesc_answer")


admin.site.register(Puesc, PuescAdmin)
