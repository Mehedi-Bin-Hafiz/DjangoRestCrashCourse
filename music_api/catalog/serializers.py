from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import  datetime
from . models import Album, Artist, Song


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


# #serializer overview
# class Comment():
#     def __init__(self,email,content, created = None):
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()
#
# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()
#
#     def create(self,validated_data):
#         return Comment(**validated_data)
#     def updagte(self,instance, validated_data):
#         instance.email = validated_data.get('email', instance)
