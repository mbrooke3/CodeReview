from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod


class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # product_ids = []
        product_ids = request.session.get('lastfivelist', [])
        product_objs = []
        for item in product_ids:
            product_objs.append(cmod.Product.objects.get(id = item))
        request.lastfivelist = product_objs

        response = self.get_response(request)

        return_ids = []
        for item2 in request.lastfivelist:
            return_ids.append(item2.id)
        request.session['lastfivelist'] = return_ids

        return response
