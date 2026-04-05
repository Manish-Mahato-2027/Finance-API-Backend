from django.urls import path
from . import views

urlpatterns = [
    path('summary/', views.DashboardSummaryView.as_view(), name='dashboard-summary'),
    path('monthly-report/', views.MonthlyReportView.as_view(), name='monthly-report'),
]