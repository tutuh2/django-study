from django.urls import path

from . import views

urlpatterns = [
    path('', views.SaerchListView.as_view(), name='search')
]
