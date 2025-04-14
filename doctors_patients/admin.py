from django.contrib import admin
from .models import PatientDoctorMapping


@admin.register(PatientDoctorMapping)
class DoctorPatientAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "doctor", "created_by", "created_at")
    search_fields = ("patient__name", "doctor__name")
    list_filter = ("created_by",)
