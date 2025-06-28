from rest_framework import serializers
from .models import Manager, Intern

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class InternSerializer(serializers.ModelSerializer):
    mentor_name = serializers.ReadOnlyField(source='mentor.name')  # Optional: show mentor name

    class Meta:
        model = Intern
        fields = '__all__'
