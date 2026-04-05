from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Transaction
from .serializers import TransactionSerializer
from .filters import TransactionFilter
from .permissions import IsAdminOrReadOnly


class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TransactionFilter
    ordering_fields = ['date', 'amount', 'created_at']

def get_queryset(self):
    if getattr(self, 'swagger_fake_view', False):
        return Transaction.objects.none()
    return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.none()  # ← add this line

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):  # ← add this guard
            return Transaction.objects.none()
        return Transaction.objects.filter(user=self.request.user)

from rest_framework import serializers

class DashboardSummarySerializer(serializers.Serializer):
    total_income = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_expense = serializers.DecimalField(max_digits=10, decimal_places=2)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)

class DashboardSummaryView(generics.GenericAPIView):
    serializer_class = DashboardSummarySerializer  # ← add this
    ...

class MonthlyReportSerializer(serializers.Serializer):
    month = serializers.CharField()
    income = serializers.DecimalField(max_digits=10, decimal_places=2)
    expense = serializers.DecimalField(max_digits=10, decimal_places=2)

class MonthlyReportView(generics.GenericAPIView):
    serializer_class = MonthlyReportSerializer  # ← add this
    ...