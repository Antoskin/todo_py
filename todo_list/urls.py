from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('switch_off/<list_id>', views.switch_off, name='switch_off'),
]
