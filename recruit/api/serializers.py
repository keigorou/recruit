from dataclasses import fields
from rest_framework import serializers
from ..models import Applicant, Recruit


class RecruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruit
        fields = '__all__'


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('recruit', 'name', 'age', 'email', 'tel')