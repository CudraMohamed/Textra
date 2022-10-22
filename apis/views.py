from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from apis.models import User
from .serializers import UserSerializer

class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
