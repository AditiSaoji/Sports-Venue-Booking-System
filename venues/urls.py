from django.urls import path
from . import views

urlpatterns = [
    path('', views.venue_list, name='venue_list'),
    path('create/', views.venue_create, name='venue_create'),
    path('<int:pk>/update/', views.venue_update, name='venue_update'),
    path('<int:pk>/delete/', views.venue_delete, name='venue_delete'),
]
