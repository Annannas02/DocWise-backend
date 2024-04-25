"""
URL configuration for docwiseproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/', include([
        path('user/', include('user.urls')),        
        path('authen/', include('authen.urls')),
        path('bodymeasurements/', include('bodymeasurements.urls')),
        path('healthdata/', include('healthdata.urls')),
        path('medication/', include('medication.urls')),
        path('profiles/', include('profiles.urls')),
        path('symptoms/', include('symptoms.urls')),
        path('reminders/', include('reminders.urls')),
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]))
]