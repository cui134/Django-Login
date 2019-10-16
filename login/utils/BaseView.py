from django.views.generic.base import View
from django.shortcuts import redirect
class AuthenticateView(View):

    @staticmethod
    def http_unauthorized(request, *args, **kwargs):
        return redirect('/login/')

    def dispatch(self, request, *args, **kwargs):

        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(),
                              self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed

        if request.user.is_authenticated:
            from login.models import UserInfo
            user = UserInfo.get_user_by_auth_user_id(request.user.id)
            if user is None:
                handler = self.http_unauthorized
            else:
                request.user_info = user
        else:
            handler = self.http_unauthorized
        return handler(request, *args, **kwargs)