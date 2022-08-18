from rest_framework import routers
from django.urls import path, include
from .views import CoreUserView


router = routers.DefaultRouter()

urlpatterns = [
    path('/', include(router.urls)),
    path('', CoreUserView.as_view(), name="teste"),
    path('sign_in/', CoreUserView.as_view(), name="sign_in"),
    ]
