from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .jwt_serializer import CustomTokenObtainPairSerializer
from .models import Player, Level
from .serializer import *


# Create your views here.
 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request, name):
    try:
        user = Player.objects.get(username=name)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_data = PlayerSerializer(user).data
    return Response(serialized_data)
 
@api_view(['POST'])
def user_signin(request):
    serializer = PlayerSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user_id": user.id,
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
#region DepricatedLogin
# @api_view(['POST'])
# def user_login(request):

#     username = request.data.get("username")
#     password = request.data.get("password")

#     user = authenticate(
#         username=username,
#         password=password
#     )

#     if user is not None:

#         refresh = RefreshToken.for_user(user)

#         return Response({
#             "message": "Login successful",
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#             "user_id": user.id,
#         })

#     return Response(
#         {"error": "Invalid username or password"},
#         status=status.HTTP_401_UNAUTHORIZED
#     )
#endregion

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['POST'])
def user_logout(request):
    return Response({"message": "Logout successful"})
     
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    try:
        user = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlayerSerializer(user)

    return Response(serializer.data)

#works 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, pk):
        try:
            user = Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if user != request.user:
            return Response(
                {"error": "Unauthorized"}, 
                status=status.HTTP_403_FORBIDDEN)
        
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_level(request):
    serializer = LevelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_level_json(request, id):
    try:
        level = Level.objects.get(id=id)
    except Level.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    return Response(level.json)
 
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_level(request, lvl_id):
    try:
        level = Level.objects.get(id=lvl_id)
    except Level.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if level.owner != request.user:
        return Response(
            {"error": "Unauthorized"},
            status=status.HTTP_403_FORBIDDEN
        )
    json_data = request.data.get("json")

    if json_data is None:
        return Response(
            {"error": "json field required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    level.save()

    return Response(
        {"message": "Level updated"},
        status=status.HTTP_200_OK
    )
 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_level(request, lvl_id):
    try:
        level = Level.objects.get(id=lvl_id)
    except Level.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if level.owner != request.user:
        return Response(
            {"error": "Unauthorized"},
            status=status.HTTP_403_FORBIDDEN
        )

    level.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
