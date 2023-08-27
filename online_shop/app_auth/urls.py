from django.urls import path
from .views import profile_view,register_view
urlpatterns = [
    path('profile/',profile_view,name='profile'),
    path('register/',register_view,name='register')

]