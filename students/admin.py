from django.contrib import admin

# Register your models here.

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_code', 'insitution', 'fName', 'sName','student_present_class')

admin.site.register(Student, StudentAdmin)