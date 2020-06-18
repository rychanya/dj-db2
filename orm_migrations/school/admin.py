from django.contrib import admin

from .models import Student, Teacher

class GroupInline(admin.TabularInline):
    model = Student.teacher.through

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [GroupInline]
