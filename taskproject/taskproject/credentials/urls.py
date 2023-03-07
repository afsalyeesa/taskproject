from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('new',views.new,name='new'),
    path('home',views.home,name='home'),
    path('form', views.form, name='form'),
    path('logout',views.logout,name='logout'),
    path('mechanical',views.mechanical,name='mechanical'),
    path('submit',views.submit,name='submit'),

]