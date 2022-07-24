from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from django.contrib.auth.models import AbstractUser
from questionnaire.models import(
    Questionnaire,
    Question,
    Answer,
    UserQuestionnaire,
    UserAnswer
)
from questionnaire.serializers import UserQuestionnaireSerializer


class UserQuestionnaireViewSet(APIView):
    serializer_class = UserQuestionnaireSerializer
    permission_classes = [AllowAny, ]
    queryset = Questionnaire.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
