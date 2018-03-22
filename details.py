from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math

@view_function
def process_request(request, product:cmod.Product):
    categories = cmod.Category.objects.all()

    if product in request.last_five:
        request.last_five.remove(product)
    request.last_five.insert(0, product)

    if len(request.last_five) > 6:
        request.last_five.pop(6)

    context= {'product': product, 'categories':categories}
    return request.dmp.render('/details.html', context)

