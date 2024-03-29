# Generated by Django 4.2.5 on 2023-09-24 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_carouselbanner_bannerimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoriesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoryName', models.CharField(blank=True, max_length=50, null=True)),
                ('subCategoryImage', models.ImageField(upload_to='media/product_images/subCategoryImg')),
            ],
        ),
    ]
