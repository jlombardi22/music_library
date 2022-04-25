from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from songs.serializer import SongsSerializer
from rest_framework import status
from songs.models import Songs
# Create your views here.


@api_view(['POST'])
def songs_list(request):

    if request.method == 'POST':
        serializer = SongsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
