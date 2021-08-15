from django.urls import path, include
from . import views
from .views import  DocumentViewSet, BudgetViewSet, CategoryViewSet, TransactionViewSet, \
    CustomObtainAuthToken
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('document', DocumentViewSet, basename='document')
router.register('budget', BudgetViewSet, basename='budget')
router.register('category', CategoryViewSet, basename='category')
router.register('transaction', TransactionViewSet, basename='transaction')


urlpatterns = [
    path('API/', include(router.urls)),
    path('API/<int:pk>', include(router.urls)),
    path('API/login/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
    path('API/signup/', views.UserCreate.as_view())

]

# Run app locally using the command 'manage.py runserver 0.0.0.0:8000' and the link to access site is http://192.168.1.154:8000/
