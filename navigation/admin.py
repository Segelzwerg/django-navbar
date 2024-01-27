from django.contrib import admin
from navigation.models import Navigation


@admin.register(Navigation)
class NavigationAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "type", "order")
    ordering = ["order"]
