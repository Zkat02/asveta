from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class Student_Admin(admin.ModelAdmin):
    list_display = ('name','amount_courses')
    search_fields = ('name',)
admin.site.register(Student, Student_Admin)


# class Subject_Admin(admin.ModelAdmin):
#     list_display = ('discipline','grade')
#     search_fields = ('grade','discipline')
# admin.site.register(Subject, Subject_Admin)


class Teacher_Admin(admin.ModelAdmin):
    list_display = ('name','education','work_experience','amount_courses')
    search_fields = ('name',)

admin.site.register(Teacher, Teacher_Admin)

class Course_Admin(admin.ModelAdmin):
    list_display = ('subject','grade','teacher','time_lesson')
    search_fields = ('subject','grade','teacher')

admin.site.register(Course, Course_Admin)
