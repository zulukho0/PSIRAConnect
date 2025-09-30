from django.contrib import admin
from .models import Course, SubjectTemplate

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'grade', 
        'description',
        'price', 
        'created_at', 
        'updated_at'
    )

    # Fields you can search by
    search_fields = ('grade',)

@admin.register(SubjectTemplate)
class SubjectTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'max_theory', 'max_practical')
    list_filter = ('course',)
    search_fields = ('name',)
