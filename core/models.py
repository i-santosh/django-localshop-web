from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CUser(AbstractUser):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    add = models.CharField(max_length=90,blank=True,null=True)
    pwd = models.CharField(max_length=1000,blank=True,null=True)
    addressBlock = models.CharField(max_length=5,blank=True,null=True)
    addressFlatNo = models.CharField(max_length=5,blank=True,null=True)
    addressCommunity = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.username

class CategoriesList(models.Model):
    categoryName = models.CharField(max_length=50,blank=True,null=True)
    categoryImage = models.ImageField(upload_to='media/product_images/categoryImg',blank=True,null=True)

    def __str__(self):
        return self.categoryName

class SubCategoriesList(models.Model):
    subCategoryName = models.CharField(max_length=50,blank=True,null=True)
    subCategoryImage = models.ImageField(upload_to="media/product_images/subCategoryImg")

    def __str__(self):
        return self.subCategoryName

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100,blank=True,null=True)
    product_quantity = models.IntegerField(default=50000000000)
    category = models.CharField(max_length=100,blank=True,null=True)
    subcategory = models.CharField(max_length=100,blank=True,null=True)
    printedPrice = models.IntegerField(default=0)
    sellingPrince = models.IntegerField(default=0)
    description = models.CharField(max_length=900,blank=True,null=True)
    pub_date = models.DateField(default=None)
    image = models.ImageField(upload_to="media/product_images/itemImg",blank=True,null=True)

    def __str__(self):
        return self.product_name

class CarouselBanner(models.Model):
    banner_id = models.AutoField
    bannerImage = models.ImageField(upload_to="media/product_images/bannerImg",default="")

    def __str__(self):
        return self.banner_id

class Order(models.Model):
    pass

class WhishList(models.Model):
    username = models.CharField(max_length=150,blank=True,null=True)
    whishListItem = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.whishListItem
