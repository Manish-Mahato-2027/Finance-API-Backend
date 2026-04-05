from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from apps.finance.models import Transaction
from apps.users.permissions import IsViewer
from .services import DashboardService


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