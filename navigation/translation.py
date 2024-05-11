"""Enables model translation for Navigation app."""

from modeltranslation.translator import register, TranslationOptions

from navigation.models import Navigation


@register(Navigation)
class NavigationTranslationOptions(TranslationOptions):
    """Enables translation for the navigation item names."""

    fields = ("name",)
