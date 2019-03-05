from django.urls import path

from . import views
app_name ='StoreTinder'
urlpatterns = [
    path('', views.index, name='index'),
    path('map_stores/', views.loadAllStoresData, name="stores_data"),
    path('detail/<int:pk>/', views.StoresDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.EditStoreView.as_view(), name="edit"),
    path('create_store/', views.CreateNewStoreView.as_view(), name="create_store"),
]