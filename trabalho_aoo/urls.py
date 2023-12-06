from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import frontpage, shop
from product.views import product
from product.views import product2
from product.views import product3
from product.views import product4

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("product.urls", namespace="product")),
    path("shop/", shop, name="shop"),
    path("product/product/", product, name="product"),
    path("product/product2/", product2, name="product2"),
    path("product/product3/", product3, name="product3"),
    path("product/product4/", product4, name="product4"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
