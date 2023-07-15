from django.urls import path
from map_app import views

app_name = 'map_app'

urlpatterns = [
    path('', views.map_view, name='map_view'),
    path('add_marker/', views.add_marker, name='add_marker'),
    path('get_markers/', views.get_markers, name='get_markers'),
    path('delete_marker/<int:marker_id>/', views.delete_marker, name='delete_marker'),
]