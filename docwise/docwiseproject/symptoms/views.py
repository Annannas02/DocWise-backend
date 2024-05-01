from rest_framework import generics
from symptoms import models, serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Symptoms
from .serializers import SymptomSerializer
from django.utils import timezone

class SymptomsList(generics.ListCreateAPIView):

    queryset = models.Symptoms.objects.all()
    serializer_class = serializers.SymptomSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_symptoms(request):
    symptoms = Symptoms.objects.filter(personid=request.user)
    serializer = SymptomSerializer(symptoms, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_symptom(request):
    user =request.user
    symptom=request.data.get('symptom')
    severity = request.data.get('severity')
    timestamp = timezone.now()

    if symptom > 0 and symptom < 20 and severity > 0 and severity < 5:
        symptomobj = models.Symptoms.objects.create(
            personid=user,
            symptom=symptom,
            severity=severity,
            timestamp=timezone.now()
        )
        
        return Response("Data created",status=status.HTTP_201_CREATED)

    else:
        return Response("Invalid data params",status=status.HTTP_400_BAD_REQUEST)
    




