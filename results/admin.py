from django.contrib import admin
from .models import Result, SubjectResult

# Register your models here.
# Inline to edit SubjectResults inside a Result
class SubjectResultInline(admin.TabularInline):
    model = SubjectResult
    extra = 0

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_instance', 'total_marks', 'average', 'status', 'submitted_at')
    inlines = [SubjectResultInline]
    list_filter = ('status', 'class_instance__course')
    search_fields = ('student__first_name', 'student__last_name', 'class_instance__batch_number')
    readonly_fields = ('total_marks', 'average')

@admin.register(SubjectResult)
class SubjectResultAdmin(admin.ModelAdmin):
    list_display = ('result', 'template', 'theory_marks', 'practical_marks', 'total_marks')
    search_fields = ('result__student__first_name', 'result__student__last_name', 'template__name')
    readonly_fields = ('total_marks',)
