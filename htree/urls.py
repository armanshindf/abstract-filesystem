from django.urls import path

from .views import base_view


urlpatterns = [
    path('show-files/', base_view)
]