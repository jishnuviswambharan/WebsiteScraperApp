from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    # path('login/facebook',views.facebook,name='facebook')
    path('logout',views.logout,name='logout')
]