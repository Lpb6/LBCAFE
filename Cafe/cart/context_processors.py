from .cart import Cart

# create context processcor to make cart work on all pages
def cart(request):
    return {'cart': Cart(request)}