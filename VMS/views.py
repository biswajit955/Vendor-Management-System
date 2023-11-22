from django.utils import timezone
from rest_framework import generics, status
from .models import Vendor, PurchaseOrder ,HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer
from rest_framework.response import Response

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class AcknowledgePurchaseOrderView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_update(self, serializer):
        instance = serializer.save(acknowledgment_date=timezone.now())
        instance.vendor.calculate_average_response_time()
        HistoricalPerformance.objects.create(
            vendor=instance.vendor,
            date=timezone.now(),
            on_time_delivery_rate=instance.vendor.calculate_on_time_delivery_rate(),
            quality_rating_avg=instance.vendor.calculate_quality_rating_avg(),
            average_response_time=instance.vendor.average_response_time,
            fulfillment_rate=instance.vendor.calculate_fulfillment_rate(),
        )

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        performance_data = {
            'on_time_delivery_rate': instance.calculate_on_time_delivery_rate(),
            'quality_rating_avg': instance.calculate_quality_rating_avg(),
            'average_response_time': instance.average_response_time,
            'fulfillment_rate': instance.calculate_fulfillment_rate(),
        }
        return Response(performance_data, status=status.HTTP_200_OK)