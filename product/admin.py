from django.contrib import admin
from .models import Category, Product, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
