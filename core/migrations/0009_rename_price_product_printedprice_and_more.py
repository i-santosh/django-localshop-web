# Generated by Django 4.2.5 on 2023-09-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_cuser_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='printedPrice',
        ),
        migrations.AddField(
            model_name='product',
            name='sellingPrince',
            field=models.IntegerField(default=0),
        ),
    ]
