from .custom_claims import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include
from .views import (
    NurseryRegisterAPIView,
    BuyerRegisterAPIView,
    BuyerList,
    UserDetail,
    NurseryList,
    login,
)
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("nurseryregister/", NurseryRegisterAPIView.as_view()),
    path("buyerregister/", BuyerRegisterAPIView.as_view()),
    path("token/obtain/", CustomTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("buyers/", BuyerList.as_view()),
    path("nurseries/", NurseryList.as_view()),
    path("users/<username>", UserDetail.as_view()),
    path("login/", login),
]
