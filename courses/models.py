from django.db import models
from user.models import User
# Create your models here.


class Courses(models.Model):
    title = models.CharField(max_length=50, default="Default Title")
    description = models.TextField(default='')
    price = models.PositiveIntegerField(default=0)
    students = models.ManyToManyField(User, verbose_name='students_on_course', related_name='student_courses')
    professors = models.ManyToManyField(User, verbose_name='professors_on_course', related_name='professor_courses')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


# class StudentsOnCourse(models.Model):
#
#     student = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Courses, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name_plural = "Students on Course"
#         unique_together = ('course', 'student')
#
#     # def save(self, *args, **kwargs):
#     #     if not self.student.is_teacher:
#     #         super().save(*args, **kwargs)
#
#
# class ProfessorsOnCourse(models.Model):
#     professor = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Courses, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name_plural = "Professors on Course"
#         unique_together = ('course', 'professor')
#
#     # def save(self, *args, **kwargs):
#     #     if self.professor.is_teacher:
#     #         super().save(*args, **kwargs)


class Lecture(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

