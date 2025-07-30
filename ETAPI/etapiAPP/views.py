from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Expense
from .serializers import ExpenseSerializer
from django.utils import timezone
from datetime import timedelta
# Create your views here.

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Expense.objects.filter(user=user)

        filter_option = self.request.query_params.get('filter')
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        now = timezone.now()

        if filter_option == 'week':
            last_week = now - timedelta(days=7)
            queryset = queryset.filter(created_at__gte=last_week)

        if filter_option == 'month':
            last_month = now - timedelta(days=30)
            queryset = queryset.filter(created_at__gte=last_month)

        if filter_option == '3months':
            last_3months = now - timedelta(days=90)
            queryset = queryset.filter(created_at__gte=last_3months)

        elif start and end:
            queryset = queryset.filter(created_at__date__range=[start, end])

        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    