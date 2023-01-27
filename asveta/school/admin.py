from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class Student_Admin(admin.ModelAdmin):
    list_display = ('user','amount_courses')
    search_fields = ('user',)
admin.site.register(Student, Student_Admin)


class Subject_Admin(admin.ModelAdmin):
    list_display = ('discipline','grade')
    search_fields = ('grade','discipline')
admin.site.register(Subject, Subject_Admin)


class Teacher_Admin(admin.ModelAdmin):
    list_display = ('user','education','work_experience','amount_courses')
    search_fields = ('user',)

admin.site.register(Teacher, Teacher_Admin)
