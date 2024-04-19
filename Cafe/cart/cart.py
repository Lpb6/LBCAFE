
class Cart():
    def __init__(self, request):
        self.session = request.session
        # gets session key if it exists
        cart = self.session.get('session__key')
        # makes new session key if there is none
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # make cart visible on all pages
        self.cart = cart