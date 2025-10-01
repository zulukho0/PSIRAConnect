from django.contrib import admin
from .models import Result, SubjectResult
from django.utils.html import format_html

# Register your models here.
# Inline to edit SubjectResults inside a Result
class SubjectResultInline(admin.TabularInline):
    model = SubjectResult
    extra = 0
    fields = ('template', 'theory_marks', 'practical_marks', 'total_marks')
    readonly_fields = ('total_marks',)  # auto-calculated
    can_delete = False

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'class_instance',
        'total_marks',
        'average',
        'status',
        'submitted_at',
        'view_report_link',
        'download_pdf_link',
    )
    list_filter = ('status', 'class_instance__course__grade')
    search_fields = ('student__first_name', 'student__last_name', 'student__id_number')
    readonly_fields = ('total_marks', 'average', 'report_file', 'created_at', 'updated_at')
    inlines = [SubjectResultInline]

    def view_report_link(self, obj):
        if obj.id:
            return format_html(
                '<a href="/results/student-report/{}/" target="_blank">View Report</a>', obj.id
            )
        return "-"
    view_report_link.short_description = "Report Page"

    def download_pdf_link(self, obj):
        if obj.report_file:
            return format_html(
                '<a href="{}" target="_blank">Download PDF</a>', obj.report_file.url
            )
        return "-"
    download_pdf_link.short_description = "Report PDF"

@admin.register(SubjectResult)
class SubjectResultAdmin(admin.ModelAdmin):
    list_display = ('result', 'template', 'theory_marks', 'practical_marks', 'total_marks')
    search_fields = ('result__student__first_name', 'result__student__last_name', 'template__name')
    readonly_fields = ('total_marks',)
