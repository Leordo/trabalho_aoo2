from django.shortcuts import render, redirect, reverse
from .models import Product, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin


# criar views:
class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("product:homeproducts")
        else:
            return super().get(self, request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse("product:login")
        else:
            return reverse("product:criarconta")


class Homeproducts(LoginRequiredMixin, ListView):
    template_name = "homeproducts.html"
    model = Product


class Detailsproduct(LoginRequiredMixin, DetailView):
    template_name = "detalhesproduct.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super(Detailsproduct, self).get_context_data(**kwargs)
        products_relacionados = Product.objects.filter(
            categoria=self.get_object().categoria
        )[0:5]
        context["products_relacionados"] = products_relacionados
        return context

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        product.visualizacoes += 1
        product.save()
        usuario = request.user
        usuario.products_vistos.add(product)
        return super().get(self, request, *args, **kwargs)


class Pesquisaproduct(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Product

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get("query")
        if termo_pesquisa:
            object_list = Product.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ["first_name", "last_name", "email"]

    def get_success_url(self):
        return reverse("product:homeproducts")


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("product:login")


def product(request):
    return render(request, "product/product.html")


def product2(request):
    return render(request, "product/product2.html")


def product3(request):
    return render(request, "product/product3.html")


def product4(request):
    return render(request, "product/product4.html")
