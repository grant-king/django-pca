from django.urls import path
from . import views    

urlpatterns = [
    path('', views.index, name='index'),
    path('configs/', views.all_configurations, name='all-configs'),
    path('configs/<int:configuration_id>/', views.configuration_detail, name='config-detail'),
    path('play/default/', views.play_default, name='play-default'),
    path('play/<int:configuration_id>/', views.play_configuration, name='run-config')
    ]