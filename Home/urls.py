from django.urls import path
from .views import home, john_mc, about

app_name = 'home'

urlpatterns = [
     path('', home, name='home'),
     path('continue/', john_mc, name='john'),
     path('about/', about, name='about'),
]