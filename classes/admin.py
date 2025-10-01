from django.contrib import admin
from .models import Class
from instructors.models import Instructor
from results.models import SubjectResult
from results.models import Result


# Register your models here.
class SubjectResultInline(admin.TabularInline):
    model = SubjectResult
    extra = 0
    fields = ('template', 'theory_marks', 'practical_marks', 'total_marks')
    readonly_fields = ('total_marks',)
    can_delete = False

class ResultInline(admin.TabularInline):
    model = Result
    extra = 0
    fields = ('student',) 
    readonly_fields = ('total_marks', 'average', 'status', 'report_file')
    inlines = [SubjectResultInline]
    show_change_link = True 

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('course', 'batch_number', 'start_date', 'end_date', 'instructor')
    filter_horizontal = ('students',)
    search_fields = ('batch_number',)
    list_filter = ('start_date', 'course')
    inlines = [ResultInline]