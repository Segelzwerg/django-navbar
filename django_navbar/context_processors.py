"""Global context provisioner."""

from django_navbar.models import Navigation, NavigationLogo


# pylint: disable=no-member
def nav_bar(_):
    """
    Provides the navigation bar for all templates.
    """
    return {
        "nav_urls": Navigation.objects.all().order_by("order"),
        "nav_logo": NavigationLogo.objects.first(),
    }
