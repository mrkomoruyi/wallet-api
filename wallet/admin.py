from django.contrib import admin
from .models import Transaction, Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'balance', 'created_at', 'updated_at']
    search_fields = ['id']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'sender', 'receiver', 'status', 'type', 'amount']
    list_filter = ['status', 'type']
    search_fields = ['id']
