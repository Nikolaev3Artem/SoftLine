from django.contrib import admin
from .models import Student, Course


class CourseStudentsInline(admin.TabularInline):
    model = Course.students.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    raw_id_fields = ['courses']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [
        CourseStudentsInline
    ]
