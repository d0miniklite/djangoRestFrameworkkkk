from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CoursesView, LectureView

router = DefaultRouter()
router.register(r'courses', CoursesView)
router.register(r'lecture', LectureView)
# router.register(r'professors_on_course', ProfessorsOnCourseView)
# router.register(r'students_on_course', StudentsOnCourseView)


urlpatterns = [
    path('', include(router.urls)),
]
