from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount_courses = models.IntegerField(default=0, verbose_name='amount of courses attended')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Subject:
    discipline = models.CharField(max_length=20)
    grade = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.discipline} : {self.grade} grade"

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Teacher:
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    education = models.CharField(blank=True)
    work_experience = models.IntegerField(blank=True) # стаж
    amount_courses = models.IntegerField(default=0, verbose_name='amount of courses conducted')

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Course(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.PROTECT)
    subject = models.OneToOneField(Subject, on_delete=models.PROTECT)
    time_lesson = models.TimeField();

class Course_Students(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
