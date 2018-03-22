from catalog import models as cmod


class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        recent_list = request.session.get('last_five', [])
        request.last_five = []

        for p in recent_list:
            request.last_five.append(cmod.Product.objects.get(id=p))

        response = self.get_response(request)

        last_five_ids = []
        for r in request.last_five:
            last_five_ids.append(r.id)       

        request.session['last_five'] = last_five_ids
        return response



    # Before the request:
    #     product_ids=session.get ids from the session
    #     products = [ convert list of ids to actual objects]
    #     request.last_five = [product objects]
    
    # in catalog/templates/base_app.htm:
    #     request.last_five

    # after the request   
    #     convert request.last_five to a list of ids
    #     set the list of ids into the session