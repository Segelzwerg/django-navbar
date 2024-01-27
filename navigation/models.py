from django.db import models


class NavigationType(models.TextChoices):
    NAV_ITEM = "nav-item"
    NAV_ITEM_DROP = "nav-item dropdown"


class Navigation(models.Model):
    name = models.CharField(max_length=50, default="")
    url = models.CharField(max_length=50, default="")
    type = models.CharField(
        max_length=50, choices=NavigationType.choices, default=NavigationType.NAV_ITEM
    )
    order = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["order"], name="order must be uniqe")
        ]
