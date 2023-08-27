
from django.urls import path , include
from . import views
from django.conf import settings
from django.contrib.auth import views as authentication_views

app_name = 'users'
urlpatterns = [
    path('register/',views.register , name='register' ),
    path('login/',authentication_views.LoginView.as_view(template_name = 'users/login.html') , name='login' ),
    path('logout/',authentication_views.LogoutView.as_view(template_name = 'users/logout.html') , name='logout' ),
    path('profile/',views.profile , name='profile' ),
    path('create_profile/',views.create_profile , name='create_profile' ),
    
    
]  