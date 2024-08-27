from django.urls import path
from .views import login_view, login_2
urlpatterns = [
    path('', login_view, name='login_view'),
    path('2Pasos/', login_2, name='2PasosVeri'),

]