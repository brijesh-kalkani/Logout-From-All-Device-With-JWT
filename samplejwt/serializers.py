from rest_framework import serializers, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import UserProfile

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(style={'input_type': 'email'})
    def validate(self, attrs):
        user = authenticate(username=attrs['username'],
                            password=attrs['password'])
        data = super().validate(attrs)
        refresh = self.get_token(user)
        refresh['username'] = user.username


        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = attrs['username']

        return data



class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(style={'input_type': 'email'})
    username = serializers.CharField(min_length=1)

    class Meta:

        model = UserProfile
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True,
                        'min_length': 8}}

    def save(self):

        account = UserProfile(email=self.validated_data['email'],
                              username=self.validated_data['username'],
                              password=self.validated_data['password']
                              )

        superuser = User.objects.create_superuser(
                    username=self.validated_data['username'],
                    email=self.validated_data['email'],
                    password=self.validated_data['password']
                )

        print(self.validated_data['email'])
        account.save()
        return account

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id','username','email', 'password')
