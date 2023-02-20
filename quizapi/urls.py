
from django.urls import path, include

from rest_framework import routers

from quizapi import views

router=routers.DefaultRouter()

router.register('users', views.MyUserViewSet)
router.register('quizs', views.QuiwViewSet)
router.register('questions', views.QuestionViewSet)
router.register('particpations', views.ParticipationViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]