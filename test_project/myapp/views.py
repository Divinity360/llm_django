from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path

token_obtain_pair = TokenObtainPairView.as_view()

