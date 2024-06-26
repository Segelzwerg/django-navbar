# Generated by Django 5.0.4 on 2024-05-04 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_navbar', '0004_navigationdropdown_and_more'),
    ]

    operations = [
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
