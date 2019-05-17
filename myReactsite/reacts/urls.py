from django.urls import path

from . import views
app_name ='reacts'
urlpatterns = [
    path('', views.index , name='index'),
]