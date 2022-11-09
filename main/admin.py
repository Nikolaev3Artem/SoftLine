from django.contrib import admin
from .models import Request, Course
from modeltranslation.admin import TranslationAdmin


class CourseRequestsInline(admin.StackedInline):
    model = Request

@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    readonly_fields = ['id',]
    inlines = [
        CourseRequestsInline
    ]
admin.site.register(Request)