from django.urls import path

from users.api.auth.views import CustomUserAuthToken

urlpatterns = [
    path('auth/', CustomUserAuthToken.as_view()),
]
