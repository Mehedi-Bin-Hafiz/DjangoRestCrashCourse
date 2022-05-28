from django.contrib.auth.models import User
from rest_framework import  viewsets
from rest_framework import  permissions
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """API Endpoint that allows user to be viewed or edited"""
    queryset = User.objects.all().order_by('-date_joined') # - means newest first oldest last
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

