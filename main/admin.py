from django.contrib import admin
from .models import Request, Course


class CourseRequestsInline(admin.StackedInline):
    model = Request

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['id',]
    inlines = [
        CourseRequestsInline
    ]
admin.site.register(Request)