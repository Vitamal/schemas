from django.contrib.auth import logout
from django.views.generic import RedirectView


class SchemasLogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        if 'oauth_token' in request.session:
            del request.session['oauth_token']
        return super(SchemasLogoutView, self).get(request, *args, **kwargs)
