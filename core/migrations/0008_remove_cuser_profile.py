# Generated by Django 4.2.5 on 2023-09-25 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_cuser_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuser',
            name='profile',
        ),
    ]
