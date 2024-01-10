from django.urls import include, path
from rest_framework import routers

from api.views import WalletViewSet, UserViewSet, TestCardViewSet

router = routers.DefaultRouter()
router.register('wallet', WalletViewSet, basename='wallet')
router.register('user', UserViewSet, basename='user')
router.register('testcards', TestCardViewSet, basename='testcards')

urlpatterns = [
    path('v1/', include(router.urls)),
]
