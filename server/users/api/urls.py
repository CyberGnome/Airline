from django.urls import path

from users.api.auth.views import CustomUserAuthToken
from users.api.register.views import CreateUserView

urlpatterns = [
    path('auth/', CustomUserAuthToken.as_view()),
    path('register/', CreateUserView.as_view()),
]
