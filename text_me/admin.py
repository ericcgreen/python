from django.contrib import admin
from . import models
# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"body": ("title",)}
admin.site.register(models.Entry)
