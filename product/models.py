from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Product(models.Model):
    categoria = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=255)
    thumb = models.ImageField(upload_to="thumb_products")
    slug = models.SlugField()
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


class Episodio(models.Model):
    product = models.ForeignKey(
        "Product", related_name="episodios", on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField()
    price = models.IntegerField()
    quantidade = models.IntegerField()
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.product.titulo + " - " + self.titulo


class Usuario(AbstractUser):
    products_vistos = models.ManyToManyField("Product")
