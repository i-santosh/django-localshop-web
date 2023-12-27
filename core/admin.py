from django.contrib import admin
from .models import CUser, Product, CarouselBanner, Order, WhishList, CategoriesList, SubCategoriesList

#Register your models here.
admin.site.register(CUser)
admin.site.register(Product)
admin.site.register(WhishList)
admin.site.register(CategoriesList)
admin.site.register(SubCategoriesList)
