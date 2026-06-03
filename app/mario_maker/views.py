from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Player, Level
from .serializer import PlayerSerializer, LevelSerializer
from decouple import config, Csv

# Create your views here.

#region users

@api_view(['GET'])
def get_user(request, name):
    try:
        user = Player.objects.get(name=name)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_data = UserSerializer(user).data
    return Response(serialized_data)


@api_view(['GET'])
def get_users(request):
    users = Player.objects.all()
    serialized_data = PlayerSerializer(users, many=True).data
    return Response(serialized_data)

@api_view(['POST'])
def user_signin(request):
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def user_login(request):
    name = request.POST["name"]
    pswrd = request.POST["hash_pswrd"]

@api_view(['PUT'])
def user_detail(request, pk):
    try:
        user = Player.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    serializer = PlayerSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request):
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

    #endregion

    #region levels

@api_view (['POST'])
def create_level(request):
    serializer = LevelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #endregion

