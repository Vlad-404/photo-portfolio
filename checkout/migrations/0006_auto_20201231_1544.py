# Generated by Django 3.1.3 on 2020-12-31 15:44

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20201231_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=20),
        ),
    ]
