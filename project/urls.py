
from django.contrib import admin
from django.urls import path
from home.views import ListUsers, RegisterUser
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', ListUsers.as_view()),
    path('api-token-auth/', views.obtain_auth_token),        
    path('register/', RegisterUser.as_view()),
]
