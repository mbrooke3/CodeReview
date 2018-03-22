from django_mako_plus import view_function, jscontext
from catalog import models as cmod

@view_function

def process_request(request, product:cmod.Product):

  # products = cmod.Product.objects.filter(id= request.dmp.urlparams[0])
    if (product in request.LastFiveList):
        request.LastFiveList.remove(product)
    request.LastFiveList.insert(0,product)

    if product.__class__.__name__ == 'BulkProduct':
        context = {
            'name': product.name,
            'description': product.description,
            'images_urls': (product.images_urls()),
            'category': product.category,
            'image_url': (product.image_url()),
            'price': product.price,
            'TITLE' : product.TITLE,
            'quantity' : product.quantity,
        }

    if product.__class__.__name__ == 'IndividualProduct':
        context = {
            'name': product.name,
            'description': product.description,
            'images_urls': (product.images_urls()),
            'category': product.category,
            'image_url': (product.image_url()),
            'price': product.price,
            'TITLE': product.TITLE,
        }

    if product.__class__.__name__ == 'RentalProduct':
        context = {
            'name': product.name,
            'description': product.description,
            'images_urls': (product.images_urls()),
            'category': product.category,
            'image_url': (product.image_url()),
            'price': product.price,
            'TITLE' : product.TITLE,
        }

    return request.dmp.render('detail.html', context)
