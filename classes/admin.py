from django.contrib import admin
from .models import Class

# Register your models here.
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('course', 'batch_number', 'start_date', 'end_date', 'created_at')
    filter_horizontal = ('students',)
    search_fields = ('batch_number',)
    list_filter = ('start_date', 'course')