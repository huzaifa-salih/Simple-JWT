from rest_framework.serializers import ModelSerializer
from .models import UserAccount


class UserAccountSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['username', 'email']
