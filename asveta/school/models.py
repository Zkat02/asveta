from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='прозвішча, імя')
    amount_courses = models.IntegerField(default=0, verbose_name='колькасць наведвальных курсаў')
    courses = models.ManyToManyField("Course",verbose_name="урок")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вучань'
        verbose_name_plural = 'Вучнi'


# class Subject(models.Model):
#     discipline = models.CharField(max_length=20)
#     grade = models.IntegerField(default=0)
#
#     # def __str__(self):
#     #     return f"{self.discipline} : {self.grade} grade"
#
#     class Meta:
#         verbose_name = 'Subject'
#         verbose_name_plural = 'Subjects'


class Teacher(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='прозвішча, імя')
    specialization = models.CharField(max_length=30, verbose_name='спецыялізацыя', blank=True)
    education = models.CharField(max_length=20, blank=True,verbose_name='адукацыя')
    work_experience = models.IntegerField(blank=True, verbose_name='стаж')
    amount_courses = models.IntegerField(default=0, verbose_name='колькасць курсаў')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Настаўнік'
        verbose_name_plural = 'Настаўнікі'


class Course(models.Model):
    subject = models.CharField(max_length=20, verbose_name='прадмет' )
    grade = models.IntegerField(default=0, verbose_name='клас')
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, verbose_name='настаўнік')
    time_lesson = models.TimeField(verbose_name='час правядзення')

    def __str__(self):
        return f"{self.subject} {self.grade} клас"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

