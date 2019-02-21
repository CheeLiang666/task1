from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('verified/', views.loadVerifiedData, name='verified'),
    path('unverified/', views.loadUnverifiedData, name='unverified'),
]