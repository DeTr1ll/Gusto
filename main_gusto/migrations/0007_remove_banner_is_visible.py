# Generated by Django 3.1.7 on 2021-02-25 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_gusto', '0006_banner_is_visible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='is_visible',
        ),
    ]
