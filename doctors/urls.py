from .views import (
    DoctorListCreateView,
    DoctorDetailView,
)
from django.urls import path

urlpatterns = [
    
    # Doctor URLs
    path("api/doctor/", DoctorListCreateView.as_view(), name="doctors"),
    path("api/doctor/<int:pk>/", DoctorDetailView.as_view(), name="doctor-detail"),
]
