
from rest_framework import viewsets 
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token 
from rest_framework.response import Response
from rest_framework.settings import api_settings
from . import permissions 
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer , ParticipationSerializer ,QuestionSerializer , QuizSerializer
from .models import User ,Quiz , Question ,Participation
from django_filters.rest_framework import DjangoFilterBackend

class MyUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateUser,)

class QuiwViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateUser,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categorie','titre']
class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class=QuestionSerializer
    queryset=Question.objects.all()
    authentication_classes =(TokenAuthentication,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quiz']
class ParticipationViewSet(viewsets.ModelViewSet):
    serializer_class=ParticipationSerializer
    queryset=Participation.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
    authentication_classes =(TokenAuthentication,)
class UserLoginApiView(ObtainAuthToken):
    """ tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                        context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.id,
            'name':user.name,
            'email':user.email
        })
