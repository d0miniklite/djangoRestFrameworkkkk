from rest_framework import viewsets
from .serializers import HomeworkSerializer, StudentsHomeworkSerializer, CommentsSerializer
from .models import Homework, StudentsHomework, Comments
from user.permissions import IsTeacher
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class HomeworkView(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = [IsAuthenticated, IsTeacher]


class StudentsHomeworkView(viewsets.ModelViewSet):
    serializer_class = StudentsHomeworkSerializer
    queryset = StudentsHomework.objects.all()


class CommentsView(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()