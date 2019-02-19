from django.urls import path

from . import views

app_name = 'kfcstores'
urlpatterns = [
    # ex: /kfcstores/
    path('', views.listing, name='index'),
    # ex: /kfcstores/4715/
    path('<int:pk>/', views.StoresDetailView.as_view(), name='detail'),
    # ex: /kfcstores/maps/
    path('maps/', views.drawKFCMap, name='maps'),
    path('maplocation/', views.getKFCsLatLng, name='maplocation'),
]