from django.contrib.auth.models import User
from rest_framework import  viewsets
from .serializers import UserSerializer, ArtistSerializer, SongSerializer
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Artist
from rest_framework import permissions
from rest_framework import  authentication
from rest_framework.generics import GenericAPIView

from rest_framework.throttling import UserRateThrottle

class OncePerDayUserThrottle(UserRateThrottle):
   rate = '/day'


class UserViewSet(viewsets.ModelViewSet):
    """API Endpoint that allows user to be viewed or edited"""
    queryset = User.objects.all().order_by('-date_joined') # - means newest first oldest last
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

##### function based view
@api_view(['GET','POST'])
def function_based(request):
    if request.method == "GET":
        return Response({"message":"GET not allowed"})
    elif request.method == "POST":
        return  Response({"message":"I am active"})
#### class based views

# class ArtistView(APIView):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     throttle_classes = [OncePerDayUserThrottle]
#
#     def get(self, request):
#         artist = Artist.objects.all()
#         return Response(artist)
#     def post(self, request):
#         return Response({'message':request.data})

class ArtistGenericView(GenericAPIView):
    queryset =  Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return
