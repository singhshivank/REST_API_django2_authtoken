from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Songs
from .serializer import SongsSerializer
import json



class ListSongsView(APIView):

    def get(self, request):
        songlist = Songs.objects.all()
        serializer = SongsSerializer(songlist, many=True)
        return Response({"songlist": serializer.data})
    
    def post(self, request, format=None):
        # song = request.data.get('songs')
        # PersonSerializer(person, data=request.DATA, partial=True)
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            song_saved = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response({"success": "Song '{}' created successfully".format(song_saved.title)})


    
