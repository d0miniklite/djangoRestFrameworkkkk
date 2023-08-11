from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from .models import Courses, Lecture
from .serializers import CoursesSerializer, LectureSerializer
from user.permissions import CustomPermissions


class CoursesView(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
    permission_classes = [CustomPermissions]


class LectureView(viewsets.ModelViewSet):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    permission_classes = [CustomPermissions]

