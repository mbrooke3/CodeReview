from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod



@view_function
def process_request(request, product:cmod.Product):
    # products = cmod.Product.objects.filter(id = request.dmp.urlparams[0])
    if (product in request.lastfivelist):
        request.lastfivelist.remove(product)
    request.lastfivelist.insert(0,product)

    return request.dmp.render(
        'details.html',
        {'p' : product}
        )
