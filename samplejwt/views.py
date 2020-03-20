from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework.decorators import api_view
from .models import UserProfile
from rest_framework import viewsets, permissions
# Create your views here.

class LoginView(TokenObtainPairView):
	"""
	Login View with jWt token authentication
	"""
	serializer_class = MyTokenObtainPairSerializer


class registrationView(APIView):

	def post(self,request,format=None):
		if request.method == 'POST':
			serializer = RegistrationSerializer(data=request.data)
			data = {}
			if serializer.is_valid():
				account = serializer.save()
				data['response'] = 'successfully registered new user.'
			else:
				data = serializer.errors
			return Response(data)

class UserProfile_view(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
