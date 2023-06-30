from django.urls import path, include
from .views import RegisterUserView, LoginUserView, RedefinePasswordView

urlpatterns = [
    path('register', RegisterUserView.as_view()),
    path('login',LoginUserView.as_view()),
    path('redefine_password', RedefinePasswordView.as_view())
    ]

