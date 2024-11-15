from django.contrib import admin
from django.urls import path, include
from venues import views

urlpatterns = [
    path('',views.venue_list),
    path('admin/', admin.site.urls),
    path('venues/', include('venues.urls')),
]
