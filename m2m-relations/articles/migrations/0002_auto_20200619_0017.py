# Generated by Django 2.2.13 on 2020-06-18 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagsarticles',
            options={'ordering': ['is_main']},
        ),
    ]
