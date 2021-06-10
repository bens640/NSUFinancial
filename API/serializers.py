from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Loan, Document, Budget, Category, Transaction


class LoanSerializer(serializers.ModelSerializer):
    # user = serializers.ForeignKey(User, on_delete=serializers.CASCADE)
    class Meta:
        model = Loan
        fields = ['name', 'amount', 'interest', 'term', 'start_date']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['title', 'type', 'link']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ['user', 'transactions']
