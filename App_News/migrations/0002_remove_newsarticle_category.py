# Generated by Django 4.2.2 on 2023-06-26 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_News', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsarticle',
            name='category',
        ),
    ]
