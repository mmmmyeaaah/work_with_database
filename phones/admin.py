from django.contrib import admin

from .models import Phone


@admin.register(Phone)
class Phoneadmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['id', 'name', 'release_date']