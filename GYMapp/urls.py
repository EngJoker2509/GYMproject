from django.urls import path
from . import views

app_name = 'GYMapp'

urlpatterns = [
    path('', views.base,name='base'),
    path('about', views.call_about, name="about"),
    path('contact', views.call_contact, name="contact"),
    path('pricing', views.call_pricing, name="price"),
    # path('hola',views.dashboard,name='dashboard'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    # path('clear', views.clear, name='clear'),
    # path('participants',views.add_participants,name='add_participants'),
]
