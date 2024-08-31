from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']  # отображаемые поля
    prepopulated_fields = {'slug': ('name',)} # автозаполнения поля slug


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'discount', 'quantity']
    list_editable = ['price', 'discount', 'quantity']  # поля для редактирования
    prepopulated_fields = {'slug': ('name',)} # автозаполнения поля slug
