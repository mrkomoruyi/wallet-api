import uuid
from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='wallet'
    )
    balance = models.DecimalField(
        max_digits=13,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [  # noqa: RUF012
            models.CheckConstraint(
                condition=Q(balance__gte=0), name='wallet_balance_gte_0'
            )
        ]


class Transaction(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        PROCESSING = 'processing', 'Processing'
        SUCCESS = 'success', 'Success'
        FAILED = 'failed', 'Failed'
        REVERSED = 'reversed', 'Reversed'

    class Type(models.TextChoices):
        TRANSFER = 'transfer', 'Transfer'
        DEPOSIT = 'deposit', 'Deposit'
        WITHDRAWAL = 'withdrawal', 'Withdrawal'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(
        Wallet, on_delete=models.PROTECT, null=True, related_name='debits'
    )
    receiver = models.ForeignKey(
        Wallet, on_delete=models.PROTECT, null=True, related_name='credits'
    )
    status = models.CharField(choices=Status, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=Type)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
