from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Player, Level
from .serializer import *
from decouple import config, Csv

# Create your views here.

#region users

@api_view(['GET'])
def get_user(request, name):
    try:user = Player.objects.get(username=name)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_data = PlayerSerializer(user).data
    return Response(serialized_data)

#works
@api_view(['POST'])
def user_signin(request):

    serializer = PlayerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user is not None:
        login(request, user)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#works
@api_view(['POST'])
def user_login(request):

    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user is not None:
        login(request, user)

        return Response({
            "message": "Login successful",
            "user_id": user.id
        })

    return Response(
        {"error": "Invalid username or password"},
        status=status.HTTP_401_UNAUTHORIZED
    )

#works
@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({"message": "Logged out"})
    
@api_view(['GET'])
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

#works
@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

    #endregion

#region levels

@api_view (['POST'])
def create_level(request):
    serializer = LevelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view (['GET'])
def get_level_infos(request, nmbr):
    if nmbr <= 0:
        return Response(
            {"error": "nmbr must be positive"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    user_id = request.GET.get("user_id")
    
    if user_id == None:
        level = Level.objects.order_by("-creation_date")[:nmbr]
    else:
        level = Level.objects.filter(owner=user_id).order_by("-creation_date")[:nmbr]

    serialized_data = LevelInfoSerializer(level, many=True).data
    return Response(serialized_data)
        
@api_view (['GET'])
def get_level_json(request, id):
    try:
        level = Level.objects.get(id=id)
    except Level.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    return Response(level.json)

@api_view(['PUT'])
def update_level(request, lvl_id):
    try:
        level = Level.objects.get(id=lvl_id)
    except Level.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    level.json = request.data["json"]
    level.save()

    return Response(
        {"message": "Level updated"},
        status=status.HTTP_200_OK
    )

@api_view(['DELETE'])
def delete_level(request, lvl_id):
    try:
        level = Level.objects.get(id=lvl_id)
    except Level.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    level.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

#endregion
