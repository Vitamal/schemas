from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse


class UserLoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_field_name = REDIRECT_FIELD_NAME
    redirect_authenticated_user = True

    @property
    def next(self):
        return self.request.POST.get('next')

    def get_success_redirect(self):
        return redirect(self.next if self.next else reverse('schemas_list'))

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.get_success_redirect()
        return super().get(request, *args, **kwargs)