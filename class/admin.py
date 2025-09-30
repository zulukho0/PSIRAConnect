from django.contrib import admin

# Register your models here.
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'start_date', 'end_date', 'created_at')
    filter_horizontal = ('students',)  # easy multi-select for students
    search_fields = ('name',)
    list_filter = ('start_date', 'course')