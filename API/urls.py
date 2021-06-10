from django.urls import path, include
# from .views import loan_list, loan_detail
from rest_framework.authtoken.views import obtain_auth_token

from .views import LoanViewSet, DocumentViewSet, BudgetViewSet, CategoryViewSet, TransactionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('loan', LoanViewSet, basename='loan')
router.register('document', DocumentViewSet, basename='document')

router.register('budget', BudgetViewSet, basename='budget')
router.register('category', CategoryViewSet, basename='category')
router.register('transaction', TransactionViewSet, basename='transaction')


urlpatterns = [
    path('API/', include(router.urls)),
    path('API/<int:pk>', include(router.urls)),
    path('API/login/', obtain_auth_token, name='api_token_auth'),
    # path('API/login/',)
    # path('api/loan/', loan_list),
    # path('api/loan/', GenericAPIView.as_view()),
    # path('api/loan/<int:id>/', GenericAPIView.as_view()),
    # path('api/loan/', LoanAPIView.as_view()),
    # path('api/loan/<int:pk>', loan_detail),
    # path('api/loan/<int:id>', LoanDetails.as_view()),
]

# Run app using manage.py runserver 0.0.0.0:8000 and the link is http://192.168.1.154:8000/
