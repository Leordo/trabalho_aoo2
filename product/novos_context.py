from product.models import Product


def lista_products_recentes(request):
    lista_products = Product.objects.all().order_by("-data_criacao")[0:8]
    if lista_products:
        product_destaque = lista_products[0]
    else:
        product_destaque = None
    return {"lista_products_recentes": lista_products, "product_destaque": product_destaque}


def lista_products_em_alta(request):
    lista_products = Product.objects.all().order_by("-visualizacoes")[0:8]
    return {"lista_products_em_alta": lista_products}
