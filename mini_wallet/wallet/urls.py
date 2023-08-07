from django.urls import path, include
from rest_framework import routers

from wallet.views.wallet import AccountViewSet

router = routers.SimpleRouter()

router.register(
    r'init',
    AccountViewSet,
    basename="account")

# router.register(
#     r'wallet',
#     WalletViewSet,
#     basename="wallet")

urlpatterns = [

    path('api/v1/', include(router.urls)),
]