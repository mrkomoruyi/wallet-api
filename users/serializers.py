from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        if validated_data['email'] == '':
            validated_data['email'] = None
        return User.objects.create(**validated_data)