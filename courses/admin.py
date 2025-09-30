from django.contrib import admin
from .models import Course, SubjectTemplate

# Register your models here.

# Inline for SubjectTemplate under Course
class SubjectTemplateInline(admin.TabularInline):
    model = SubjectTemplate
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('grade', 'description', 'price', 'created_at')
    inlines = [SubjectTemplateInline]
    search_fields = ('grade',)

# Register SubjectTemplate separately to allow direct access
@admin.register(SubjectTemplate)
class SubjectTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'max_theory', 'max_practical')
    list_filter = ('course',)
    search_fields = ('name',)
