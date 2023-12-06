from django.contrib import admin
from django.urls import path, include
from product.views import (
    Homepage,
    Homeproducts,
    Detailsproduct,
    Pesquisaproduct,
    Paginaperfil,
    Criarconta,
)
from django.contrib.auth import views as auth_view

app_name = "product"

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("product/", Homeproducts.as_view(), name="homeproducts"),
    path("product/<int:pk>", Detailsproduct.as_view(), name="detailsproduct"),
    path("pesquisa/", Pesquisaproduct.as_view(), name="pesquisaproduct"),
    path("login/", auth_view.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("editarperfil/<int:pk>", Paginaperfil.as_view(), name="editarperfil"),
    path("criarconta/", Criarconta.as_view(), name="criarconta"),
]
