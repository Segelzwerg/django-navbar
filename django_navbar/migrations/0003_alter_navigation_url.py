# Generated by Django 5.0.1 on 2024-01-27 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_navbar', '0002_navigation_name_navigation_order_navigation_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigation',
            name='url',
            field=models.CharField(default='', max_length=50),
        ),
    ]
