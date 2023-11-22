from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, **kwargs):
    instance.vendor.calculate_on_time_delivery_rate()
    instance.vendor.calculate_quality_rating_avg()
    instance.vendor.calculate_average_response_time()
    instance.vendor.calculate_fulfillment_rate()
