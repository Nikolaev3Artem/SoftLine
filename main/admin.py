from django.contrib import admin
from .models import Request, Course


class CourseRequestsInline(admin.StackedInline):
    model = Request


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    raw_id_fields = ['course']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
    inlines = [
        CourseRequestsInline
    ]
