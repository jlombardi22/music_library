from django.shortcuts import get_object_or_404, render
from songs.models import Songs
from rest_framework.decorators import api_view
from rest_framework.response import Response
from songs.serializer import SongsSerializer
from rest_framework import status

# Create your views here.


@api_view(['POST', 'GET'])
def songs_list(request):

    if request.method == 'POST':
        serializer = SongsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def songs_detail(request, pk):
    song = get_object_or_404(Songs, pk=pk)
    if request.method == 'GET':
        serializer = SongsSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongsSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response(stauts=status.HTTP_200_OK)
