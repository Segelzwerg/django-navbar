# Generated by Django 5.0.6 on 2024-06-27 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('django_navbar', '0001_initial'), ('django_navbar', '0002_navigation_name_navigation_order_navigation_type_and_more'), ('django_navbar', '0003_alter_navigation_url'), ('django_navbar', '0004_navigationdropdown_and_more'), ('django_navbar', '0005_navlogo_alter_navigation_type_and_more')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('order', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('nav-item', 'Nav Item'), ('nav-item dropdown', 'Nav Item Drop')], default='nav-item', max_length=50)),
                ('url', models.URLField(default='')),
            ],
        ),
        migrations.AddConstraint(
            model_name='navigation',
            constraint=models.UniqueConstraint(fields=('order',), name='order must be uniqe'),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='url',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.CreateModel(
            name='NavigationDropDown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('url', models.CharField(default='', max_length=50)),
                ('type', models.CharField(choices=[('nav-item', 'Nav Item'), ('nav-item dropdown', 'Nav Item Drop'), ('dropdown-item', 'Drop Down Item')], default='nav-item', max_length=50)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='navigation',
            name='order must be uniqe',
        ),
        migrations.AlterField(
            model_name='navigation',
            name='type',
            field=models.CharField(choices=[('nav-item', 'Nav Item'), ('nav-item dropdown', 'Nav Item Drop'), ('dropdown-item', 'Drop Down Item')], default='nav-item', max_length=50),
        ),
        migrations.AddConstraint(
            model_name='navigation',
            constraint=models.UniqueConstraint(fields=('order',), name='navigation_order_unique'),
        ),
        migrations.AddField(
            model_name='navigationdropdown',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DropDownRelation', to='navigation.navigation'),
        ),
        migrations.AddConstraint(
            model_name='navigationdropdown',
            constraint=models.UniqueConstraint(fields=('parent', 'order'), name='dropdown_order_unique'),
        ),
        migrations.CreateModel(
            name='NavLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('url', models.CharField(default='', max_length=50)),
                ('src', models.CharField(default='', max_length=50)),
                ('alt_text', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='navigation',
            name='type',
            field=models.CharField(choices=[('nav-logo', 'Nav Logo'), ('nav-item', 'Nav Item'), ('nav-item dropdown', 'Nav Item Drop'), ('dropdown-item', 'Drop Down Item')], default='nav-item', max_length=50),
        ),
        migrations.AlterField(
            model_name='navigationdropdown',
            name='type',
            field=models.CharField(choices=[('nav-logo', 'Nav Logo'), ('nav-item', 'Nav Item'), ('nav-item dropdown', 'Nav Item Drop'), ('dropdown-item', 'Drop Down Item')], default='nav-item', max_length=50),
        ),
    ]
