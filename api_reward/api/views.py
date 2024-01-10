from rest_framework import viewsets, permissions

from reward.models import TestCard, User, Wallet
from .serializers import TestCardSerializer, WalletSerializer, UserSerializer
from .permissions import UserOrReadOnly, AuthorOrReadOnly
from rest_framework.exceptions import ValidationError


class WalletViewSet(viewsets.ModelViewSet):
    '''Representation for the Wallet model'''
    serializer_class = WalletSerializer
    permission_classes = (UserOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        if Wallet.objects.filter(user=user).exists():
            raise ValidationError("The Wallet already exists for this user")

        serializer.save(user=user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''Representation for the User model'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class TestCardViewSet(viewsets.ModelViewSet):
    '''Representation for the TestCard model'''
    serializer_class = TestCardSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return TestCard.objects.filter(author=user)

    def perform_create(self, serializer):
        # First, we save the serializer object
        test_card = serializer.save(author=self.request.user)

        # We get the user who added the test card
        user = self.request.user

        # Getting an instance of the user's Wallet model
        wallet = Wallet.objects.get(user=user)

        # Increasing the value of wallet_balance by 1
        wallet.wallet_balance += 1

        # We save the updated data of the Wallet model
        wallet.save()

        # Returning the created instance of the Test Card
        return test_card
