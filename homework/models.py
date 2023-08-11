from django.db import models
from courses.models import Lecture
from user.models import User
# Create your models here.


class Homework(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class StudentsHomework(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    submitted = models.BooleanField(default=False)
    graded = models.BooleanField(default=False)
    grade = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Student: {self.student.username}, Homework: {self.homework.title}"


class Comments(models.Model):
    student_homework = models.ForeignKey(StudentsHomework, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"Comment on: {self.student_homework}"

