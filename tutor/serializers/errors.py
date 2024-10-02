from rest_framework import serializers
from django.db.models import Count
from django.utils import timezone

from tutor.models import Error, User

from .users import UserSerializer


class ErrorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.UUIDField(write_only=True, required=True)
    class Meta:
        model = Error
        fields = (
            'id',
            'user',
            'user_id',
            'errorCategory',
            'errorSubCategory',
            'timestamp_utc',
        )
        read_only_fields = (
            'id',
            'timestamp_utc',
        )

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        if user is None:
            raise serializers.ValidationError('User not found')
        error = Error.objects.create(user=user, **validated_data)
        return error


class ErrorFilterSerializer(serializers.Serializer):
    user_id = serializers.UUIDField(required=True)
    last_n_days = serializers.IntegerField(min_value=1, required=False)
    top_n_errors = serializers.IntegerField(min_value=1, required=False)

class TopErrorSerializer(serializers.Serializer):
    errorCategory = serializers.CharField()
    errorSubCategory = serializers.CharField()
    errorFrequency = serializers.IntegerField()

class TopErrorResponseSerializer(serializers.Serializer):
    top_errors = TopErrorSerializer(many=True)
