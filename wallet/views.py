from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from .models import Wallet
from .serializers import WalletSerializer

class WalletViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
