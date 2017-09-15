from django.contrib import admin
from .models import Course, Discipline
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    model=Course


class DisciplineAdmin(admin.ModelAdmin):
    model=Discipline


admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Course, CourseAdmin)
