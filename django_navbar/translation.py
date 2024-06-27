"""Enables model translation for Navigation app."""

from modeltranslation.translator import register, TranslationOptions

from django_navbar.models import Navigation, NavigationDropDown, NavigationLogo


@register(Navigation)
class NavigationTranslationOptions(TranslationOptions):
    """Enables translation for the navigation item names."""

    fields = ("name",)


@register(NavigationDropDown)
class NavigationTypeTranslationOptions(TranslationOptions):
    """Enables translation for the navigation dropdown item names."""

    fields = ("name",)


@register(NavigationLogo)
class NavigationLogoTranslationOptions(TranslationOptions):
    """Enables translation for the navigation logo item names."""

    fields = ("name", "alt_text")
