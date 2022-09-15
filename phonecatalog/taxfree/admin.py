from django.contrib import admin
from taxfree.models import Puesc
from .models import *

class TaxfreeAdmin(admin.ModelAdmin):
    list_display = ("taxid","puesc_answer")
    search_fields = ("taxid", "puesc_answer")
    list_filter = ("taxid", "puesc_answer")

admin.site.register(Puesc, TaxfreeAdmin)
