from django.db import models


class NavigationType(models.TextChoices):
    NAV_LOGO = "nav-logo"
    NAV_ITEM = "nav-item"
    NAV_ITEM_DROP = "nav-item dropdown"
    DROP_DOWN_ITEM = "dropdown-item"


class Navigation(models.Model):
    name = models.CharField(max_length=50, default="")
    url = models.CharField(max_length=50, default="")
    type = models.CharField(
        max_length=50, choices=NavigationType.choices, default=NavigationType.NAV_ITEM
    )
    order = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["order"], name="navigation_order_unique")
        ]

    @property
    def get_children(self):
        return NavigationDropDown.objects.filter(parent=self).order_by("order")


class NavigationDropDown(models.Model):
    name = models.CharField(max_length=50, default="")
    url = models.CharField(max_length=50, default="")
    type = models.CharField(
        max_length=50, choices=NavigationType.choices, default=NavigationType.NAV_ITEM
    )
    order = models.IntegerField(default=0)
    parent = models.ForeignKey(
        Navigation, on_delete=models.CASCADE, related_name="DropDownRelation"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["parent", "order"], name="dropdown_order_unique"
            )
        ]


class NavLogo(models.Model):
    """
    Logo in the navigation bar.
    :param name: name of the logo
    :param src: url to the image
    :param url: target url if clicked
    :param alt_text: alternative text if image cannot be displayed
    """

    name = models.CharField(max_length=50, default="")
    url = models.CharField(max_length=50, default="")
    src = models.CharField(max_length=50, default="")
    alt_text = models.CharField(max_length=50, default="")
