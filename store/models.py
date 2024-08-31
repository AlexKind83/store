from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        ordering = ['name']  # сортировка
        indexes = [models.Index(fields=['name']),]  # поиск
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категорий'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Автоматизация url адресов"""
        return reverse('store:category_slug', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='product_images', blank=True, null=True, verbose_name='Изображение')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    class Meta:
        db_table = 'product'
        ordering = ['name']  # сортировка записи
        indexes = [models.Index(fields=['id', 'slug']), models.Index(fields=['name']),]  # поиск по индексам
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.name} Количество - {self.quantity}"

    def display_id(self):
        return f"{self.id:03}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100)
        return self.price

    def get_absolute_url(self):
        """Автоматизация url адресов"""
        return reverse('store:product_detail', args=[self.pk, self.slug])
