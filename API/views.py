import datetime

from django.contrib.auth.models import User
from django.db.models import Prefetch
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Document, Budget, Category, Transaction
from .serializers import DocumentSerializer, TransactionSerializer, CategorySerializer, \
    BudgetSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny


class DocumentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class BudgetViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, ):
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetSerializer
    queryset = Budget.objects.prefetch_related(
        Prefetch('transactions', queryset=Transaction.objects.order_by('-transaction_date')))

    today = datetime.date.today()

    Transaction.objects.filter(date_created=today).order_by('date_created')


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TransactionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin, ):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})
