# Generated by Django 3.1.2 on 2020-10-27 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quick_link', '0003_auto_20201027_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrol',
            name='image',
        ),
    ]
