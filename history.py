from django_mako_plus import view_function, jscontext
from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        product_ids = request.session.get('LastFiveList', [])
        product_objs = []

        for item in product_ids:
            product_objs.append(cmod.Product.objects.get(id = item))

        request.LastFiveList = product_objs

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return_ids = []

        for item2 in request.LastFiveList:
            return_ids.append(item2.id)

        request.session['LastFiveList'] = return_ids

        return response
