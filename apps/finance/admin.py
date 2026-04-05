from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'transaction_type', 'category', 'date', 'created_at')
    list_filter = ('transaction_type', 'category', 'date', 'user')
    search_fields = ('description', 'user__username')
    ordering = ('-date',)