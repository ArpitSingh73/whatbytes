from django.urls import path
from .views import PatientListCreateView, PatientDetailView

urlpatterns = [
    path("api/patient/", PatientListCreateView.as_view(), name="patients"),
    path("api/patient/<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),
]
