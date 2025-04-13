from .models import Doctor
from rest_framework import serializers
# from django.contrib.auth.models import User   # Assuming you have a User model for authentication


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id", "name", "specialization", "contact", "bio", "created_at"]
