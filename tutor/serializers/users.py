from rest_framework import serializers

from tutor.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )