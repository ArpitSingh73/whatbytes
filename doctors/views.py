from .models import  Doctor
from .serializers import  DoctorSerializer
from rest_framework import status, permissions
from rest_framework.response import Response    
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Patient views are already defined...


class DoctorListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        doctors = Doctor.objects.filter(created_by=request.user)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        return get_object_or_404(Doctor, pk=pk, created_by=user)

    def get(self, request, pk):
        doctor = self.get_object(pk, request.user)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk):
        doctor = self.get_object(pk, request.user)
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doctor = self.get_object(pk, request.user)
        doctor.delete()
        return Response(
            {"message": "Doctor record deleted."}, status=status.HTTP_204_NO_CONTENT
        )
