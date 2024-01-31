from django.urls import reverse
from oauthlib.oauth2 import NoAuthToken
from django.utils.functional import SimpleLazyObject


class CognitoAuthMiddleware(
    CognitoAuthenticationMixin, middleware.AuthenticationMiddleware
):
    @staticmethod
    def get_auth_token(request):
        try:
            return request.META["HTTP_AUTHORIZATION"]
        except Exception:
            raise NoAuthToken()

    def process_request(self, request):
        if request.path.startswith(reverse("admin:index")):
            return None
        request.user = SimpleLazyObject(lambda: self.authenticate(request))
