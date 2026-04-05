from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from apps.finance.models import Transaction
from datetime import datetime, timedelta


class DashboardService:
    def __init__(self, user):
        self.user = user

    def get_summary(self):
        transactions = Transaction.objects.filter(user=self.user)

        total_income = transactions.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        total_expense = transactions.filter(transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
        balance = total_income - total_expense

        # Current month
        current_month = datetime.now().month
        current_year = datetime.now().year
        monthly_income = transactions.filter(
            transaction_type='income',
            date__year=current_year,
            date__month=current_month
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        monthly_expense = transactions.filter(
            transaction_type='expense',
            date__year=current_year,
            date__month=current_month
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        return {
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance,
            'monthly_income': monthly_income,
            'monthly_expense': monthly_expense,
        }

    def get_monthly_report(self):
        # Last 12 months
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)

        monthly_data = Transaction.objects.filter(
            user=self.user,
            date__range=[start_date, end_date]
        ).annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            income=Sum('amount', filter={'transaction_type': 'income'}),
            expense=Sum('amount', filter={'transaction_type': 'expense'}),
            count=Count('id')
        ).order_by('month')

        return list(monthly_data)