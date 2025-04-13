from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class MappingListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        mappings = PatientDoctorMapping.objects.filter(created_by=request.user)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientDoctorMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MappingByPatientView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, patient_id):
        mappings = PatientDoctorMapping.objects.filter(
            patient__id=patient_id, created_by=request.user
        )
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data)


class MappingDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        mapping = get_object_or_404(
            PatientDoctorMapping, pk=pk, created_by=request.user
        )
        mapping.delete()
        return Response(
            {"message": "Mapping deleted."}, status=status.HTTP_204_NO_CONTENT
        )
