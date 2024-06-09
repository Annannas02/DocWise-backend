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
from django.utils.timezone import make_aware
from datetime import datetime

class HealthDataList(generics.ListCreateAPIView):

    queryset = models.HealthData.objects.all()
    serializer_class = serializers.HealthDataSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_health_statistics(request):
    user = request.user
    from_date_str = request.data.get('from_date')
    to_date_str = request.data.get('to_date')

    if from_date_str and to_date_str:
        try:
            from_date = make_aware(datetime.strptime(from_date_str, '%Y-%m-%d'))
            to_date = make_aware(datetime.strptime(to_date_str, '%Y-%m-%d'))
        except ValueError:
            return Response({"detail": "Invalid date format. Date format should be YYYY-MM-DD."}, status=400)
        
        healthdata = models.HealthData.objects.filter(personid=user.id, timestamp__range=(from_date, to_date)).order_by('timestamp')
    else:
        healthdata = models.HealthData.objects.filter(personid=user.id).order_by('timestamp')

    serialized_data = serializers.HealthDataSerializer(healthdata, many=True)

    return Response(serialized_data.data, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_latest_health(request):

    user = request.user
    latest_healthdata = models.HealthData.objects.filter(personid=user.id).order_by('-timestamp').first()

    if latest_healthdata is not None:

        serialized_data = serializers.HealthDataSerializer(latest_healthdata)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "No health data found for this user"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_health_data(request):

    user = request.user

    temperature = request.data.get("temperature")
    oxygen = request.data.get("oxygen")
    pulse = request.data.get("pulse")
    timestamp=request.data.get("timestamp")

    if timestamp is None:
        timestamp=timezone.now()

    if temperature > 35.0 and temperature <= 42.0 and pulse > 30 and pulse <= 200 and oxygen >= 70 and oxygen < 100:
        healthdata = models.HealthData.objects.create(
            personid=user,
            temperature=temperature,
            oxygen=oxygen,
            pulse=pulse,
            timestamp=timestamp
        )
        
        return Response("Data created",status=status.HTTP_201_CREATED)

    else:
        return Response("Invalid data params",status=status.HTTP_400_BAD_REQUEST)
    


