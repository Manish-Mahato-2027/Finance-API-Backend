from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from apps.finance.models import Transaction
from apps.users.permissions import IsViewer
from .services import DashboardService
from rest_framework import serializers


class DashboardSummaryView(generics.GenericAPIView):
    permission_classes = [IsViewer]

    def get(self, request):
        user = request.user
        service = DashboardService(user)
        data = service.get_summary()
        return Response(data)


class MonthlyReportView(generics.GenericAPIView):
    permission_classes = [IsViewer]

    def get(self, request):
        user = request.user
        service = DashboardService(user)
        data = service.get_monthly_report()
        return Response(data)
    

   

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
    serializer_class = MonthlyReportSerializer  
    ...