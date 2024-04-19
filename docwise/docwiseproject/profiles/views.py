from rest_framework import generics
from profiles import models, serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404

class ProfileList(generics.ListCreateAPIView):
    #permission_classes = [IsAdminUser]
    #authentication_classes = [TokenAuthentication]
    
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def modify_profile(request):
    user = request.user
    profile = models.Profile.objects.filter(personid=user).update(
        name = request.data.get("name"),
        surname = request.data.get("surname"),
        gender_type = request.data.get("gender"),
        img = request.data.get("photo"),
        dob = request.data.get("dob")
        )
    return Response(status=status.HTTP_200_OK)

    