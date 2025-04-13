from .views import (
     
    MappingListCreateView,
    MappingByPatientView,
    MappingDeleteView,
)
from django.urls import path

urlpatterns = [
     
    # Mapping APIs
    path("mappings/", MappingListCreateView.as_view(), name="mappings"),
    path("mappings/<int:patient_id>/",
        MappingByPatientView.as_view(),
        name="mapping-by-patient",
    ),
    path("mappings/delete/<int:pk>/",
        MappingDeleteView.as_view(),
        name="delete-mapping",
    ),
]
