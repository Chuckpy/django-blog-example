from rest_framework import routers
from django.urls import path, include
from .views import HomeBlogView


router = routers.DefaultRouter()

urlpatterns = [
    # path('/', include(router.urls)),
    path('', HomeBlogView.as_view(), name="blog_home"),

]
