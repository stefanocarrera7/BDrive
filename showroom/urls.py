from django.urls import path
from . import views

app_name = 'showroom'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('car/<slug:slug>/', views.detail, name='detail'),
    path('contacts/', views.contacts, name='contacts'),
]
