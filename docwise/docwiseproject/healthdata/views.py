from rest_framework import generics
from healthdata import models, serializers
from user.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils import timezone

class HealthDataList(generics.ListCreateAPIView):

    queryset = models.HealthData.objects.all()
    serializer_class = serializers.HealthDataSerializer

@api_view(['POST'])
def get_health_by_username(request):
    # Retrieve the user by username, return 404 if not found
    user = get_object_or_404(User, username=request.data.get("username"))

    # Retrieve all health data objects associated with the user
    healthdata = models.HealthData.objects.filter(personid=user.id)
    
    # Serialize the health data objects
    serialized_data = serializers.HealthDataSerializer(healthdata, many=True)
    
    # Return the serialized data
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_latest_health_by_username(request):
    # Retrieve the user by username, return 404 if not found
    print(request.data.get("username"))
    user = User.objects.get(username=request.data.get("username"))

    # Retrieve the latest health data object associated with the user
    latest_healthdata = models.HealthData.objects.filter(personid=user.id).order_by('-timestamp').first()

    if latest_healthdata is not None:
        # Serialize the latest health data object
        serialized_data = serializers.HealthDataSerializer(latest_healthdata)
        # Return the serialized data
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    else:
        # Return 404 if no health data is found for the user
        return Response({"detail": "No health data found for this user"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def add_health_data(request):
    try:
        user = User.objects.get(username=request.data.get("username"))

    except:
        return Response("No such user exists.", status=status.HTTP_404_NOT_FOUND)
    temperature = request.data.get("temperature")
    oxygen = request.data.get("oxygen")
    pulse = request.data.get("pulse")

    if temperature > 35.0 and temperature <= 42.0 and pulse > 30 and pulse <= 200 and oxygen >= 70 and oxygen < 100:
        healthdata = models.HealthData.objects.create(
            personid=user,
            temperature=temperature,
            oxygen=oxygen,
            pulse=pulse,
            timestamp=timezone.now()
        )
        
        return Response("Data created",status=status.HTTP_201_CREATED)

    else:
        return Response("Invalid data params",status=status.HTTP_400_BAD_REQUEST)
    


