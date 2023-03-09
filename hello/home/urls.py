from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    
]
