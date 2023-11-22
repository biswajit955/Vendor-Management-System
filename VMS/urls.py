from django.urls import path
from .views import (
    VendorListCreateView,
    VendorRetrieveUpdateDeleteView,
    PurchaseOrderListCreateView,
    PurchaseOrderRetrieveUpdateDeleteView,
    AcknowledgePurchaseOrderView,
    VendorPerformanceView,
    CustomObtainAuthToken,
    LogoutView,
    SignupView
)

urlpatterns = [
    path('api/token/', CustomObtainAuthToken.as_view(), name='obtain-token'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/signup/', SignupView.as_view(), name='signup'),

    path('api/vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
    path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDeleteView.as_view(), name='purchase-order-retrieve-update-delete'),
    path('api/vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('api/purchase_orders/<int:pk>/acknowledge/', AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),
]