from rest_framework import serializers
from reward.models import TestCard, User, Wallet


class WalletSerializer(serializers.ModelSerializer):
    '''Sterilizer for the Wallet model'''

    class Meta:
        model = Wallet
        fields = '__all__'
        read_only_fields = ('user',)


class TestCardSerializer(serializers.ModelSerializer):
    '''Sterilizer for the TestCard model'''

    class Meta:
        model = TestCard
        fields = '__all__'
        read_only_fields = ('author',)


class UserSerializer(serializers.ModelSerializer):
    '''Sterilizer for the User model'''

    class Meta:
        model = User
        fields = '__all__'
