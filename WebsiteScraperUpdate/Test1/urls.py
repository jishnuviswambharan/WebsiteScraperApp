from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "test1"

urlpatterns = [
    # path('home',views.home, name='home'),
    path('',views.index, name='index'),
]


# Serve media files during development
