# Generated by Django 3.1.7 on 2021-03-15 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_neighbors_api', '0006_auto_20210315_0013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chefrating',
            options={'verbose_name': 'rating_chef', 'verbose_name_plural': 'ratings_chef'},
        ),
        migrations.AlterModelOptions(
            name='menurating',
            options={'verbose_name': 'rating_menu', 'verbose_name_plural': 'ratings_menu'},
        ),
    ]