# Generated by Django 3.1.7 on 2021-02-25 08:52

from django.db import migrations, models
import main_gusto.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_gusto', '0004_auto_20210225_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to=main_gusto.models.Banner.get_file_name_banners)),
            ],
        ),
    ]