from django.contrib import admin
from navigation.models import Navigation, NavigationDropDown


@admin.register(Navigation)
class NavigationAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "type", "order")
    ordering = ["order"]


@admin.register(NavigationDropDown)
class NavigationDropDownAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "type", "order", "parent")
    ordering = ["order"]
