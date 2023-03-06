from rest_framework import serializers

from ..models import VerificationCode


class VerificationCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VerificationCode
        fields = ['user', 'verification_code']
