from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Loan, Document, Budget, Category, Transaction
from .serializers import LoanSerializer, DocumentSerializer, TransactionSerializer, CategorySerializer, BudgetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class LoanViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()


class DocumentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class BudgetViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TransactionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


# class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
#                      mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
#                      mixins.DestroyModelMixin):
#     serializer_class = LoanSerializer
#     queryset = Loan.objects.all()
#     lookup_field = 'id'
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#     def put(self, request, id=None):
#         return self.update(request, id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)
#
#
# class LoanAPIView(APIView):
#     def get(self, request):
#         loans = Loan.objects.all()
#         serializer = LoanSerializer(loans, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = LoanSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class LoanDetails(APIView):
#     def get_object(self, id):
#         try:
#             return Loan.objects.get(id=id)
#         except Loan.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, id):
#         loan = self.get_object(id)
#         serializer = LoanSerializer(loan)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         loan = self.get_object(id)
#         serializer = LoanSerializer(loan, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         loan = self.get_object(id)
#         loan.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def loan_list(request):
#     if request.method == 'GET':
#         loans = Loan.objects.all()
#         serializer = LoanSerializer(loans, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#
#         serializer = LoanSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def loan_detail(request, pk):
#     try:
#         loan = Loan.objects.get(pk=pk)
#     except Loan.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = LoanSerializer(loan)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#
#         serializer = LoanSerializer(loan, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         loan.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
