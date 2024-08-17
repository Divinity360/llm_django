from django.urls import path
from . import views

urlpatterns = [
    path('api/token/', views.token_obtain_pair, name='token_obtain_pair'),
]
