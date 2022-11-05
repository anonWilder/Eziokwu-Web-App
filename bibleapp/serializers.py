from rest_framework import serializers
from .models import *

class categorySerializer(serializers.ModelSerializer):
    # student_name = serializers.CharField(source='student',read_only=True)
    # subject_name = serializers.CharField(source='subject',read_only=True)
    # semester_name = serializers.CharField(source='semester',read_only=True)

    class Meta:
        model = category
        fields = [
            'name',
        ]

class subcategorySerializer(serializers.ModelSerializer):
    # student_name = serializers.CharField(source='student',read_only=True)
    # subject_name = serializers.CharField(source='subject',read_only=True)
    # semester_name = serializers.CharField(source='semester',read_only=True)

    class Meta:
        model = subcategory
        fields = [
            'category',
            'name',
        ]

class headerSerializer(serializers.ModelSerializer):
    # student_name = serializers.CharField(source='student',read_only=True)
    # subject_name = serializers.CharField(source='subject',read_only=True)
    # semester_name = serializers.CharField(source='semester',read_only=True)

    class Meta:
        model = header
        fields = [
            'subcategory',
            'header',
            'description'
        ]