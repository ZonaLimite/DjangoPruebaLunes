from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import CountryViewSet

router = DefaultRouter()
router.register(r"countries", CountryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('dimehora/', views.view_damehora),
    path('welcome/<str:name>/', views.view_helloworld)
]