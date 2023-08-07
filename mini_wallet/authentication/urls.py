from django.urls import path, include
from rest_framework import routers

from authentication.views.login import LoginViewSet

router = routers.SimpleRouter()

router.register(
    r'',
    LoginViewSet,
    basename="registration")

urlpatterns = [

    path('api/v1/', include(router.urls)),
]