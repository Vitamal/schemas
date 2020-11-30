from django.contrib.auth import logout
from django.views.generic import RedirectView

from schemas.project.default.settings import LOGIN_URL


class SchemasLogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = LOGIN_URL

    def get(self, request, *args, **kwargs):
        logout(request)
        if 'oauth_token' in request.session:
            del request.session['oauth_token']
        return super(SchemasLogoutView, self).get(request, *args, **kwargs)
