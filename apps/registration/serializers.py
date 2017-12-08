from rest_framework import serializers

from apps.registration.models import Application, ApplicationField


class ApplicationFieldSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ApplicationField
        fields = ("ordering", "type", "options", "char_limit", "prompt")
        read_only_fields = fields


class ApplicationSchemaSerializer(serializers.ModelSerializer):
    fields = ApplicationFieldSerializer(many=True)

    class Meta:
        model = Application
        fields = ("hackathon", "status", "fields")
        read_only_fields = fields