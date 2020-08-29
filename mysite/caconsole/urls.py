from django.urls import path
from . import views    

urlpatterns = [
    path('', views.index, name='index'),
    path('configs/', views.all_configurations, name='all-configs')
    ]