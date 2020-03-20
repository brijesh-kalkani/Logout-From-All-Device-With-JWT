from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class UserProfile(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email",max_length=60, unique=True,blank=True,default='Null')
	username 				= models.CharField(max_length=30,default='Null')
	password 				= models.CharField(verbose_name='password',max_length=16)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return self.email
