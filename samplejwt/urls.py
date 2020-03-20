from django.urls import path,include
from .views import *
from samplejwt import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('view', UserProfile_view,basename='view')

urlpatterns = [

    path('login/', LoginView.as_view(), name='customelogin'),
    path('register/', registrationView.as_view(), name='customeregistration'),
    # path('view', UserProfile_view.as_view(),name='view'),
    path('new', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
