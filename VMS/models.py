from django.utils import timezone
from django.db import models
from django.db.models import Count, Case, When, F, Value, FloatField

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
    def calculate_on_time_delivery_rate(self):
        completed_pos = self.purchase_orders.filter(status='completed')
        total_completed_pos = completed_pos.count()

        if total_completed_pos == 0:
            return 0

        on_time_deliveries = completed_pos.filter(delivery_date__lte=timezone.now()).count()
        return (on_time_deliveries / total_completed_pos) * 100
    
    def calculate_quality_rating_avg(self):
        completed_pos_with_rating = self.purchase_orders.filter(status='completed', quality_rating__isnull=False)
        total_ratings = completed_pos_with_rating.aggregate(total_ratings=models.Sum('quality_rating'))['total_ratings']
        total_completed_pos = completed_pos_with_rating.count()
        return total_ratings / total_completed_pos if total_completed_pos > 0 else 0

    def calculate_average_response_time(self):
        completed_pos_with_acknowledgment = self.purchase_orders.filter(
            status='completed', acknowledgment_date__isnull=False
        )
        response_times = (
            completed_pos_with_acknowledgment.annotate(
                response_time=models.ExpressionWrapper(
                    models.F('acknowledgment_date') - models.F('issue_date'), output_field=models.DurationField()
                )
            )
            .aggregate(average_response_time=models.Avg('response_time'))
        )['average_response_time']
        self.average_response_time = response_times.total_seconds() / 60 if response_times else 0
        self.save()

    def calculate_fulfillment_rate(self):
        # total_pos = self.purchase_orders.count()
        # print(total_pos)
        # successful_pos = self.purchase_orders.filter(status='completed', status__isnull=True).count()

        # return (successful_pos / total_pos) * 100 if total_pos > 0 else 0
    
        total_pos = self.purchase_orders.count()

        if total_pos == 0:
            return 0

        successful_pos = self.purchase_orders.filter(status='completed', status__isnull=True).aggregate(
            successful_pos=Count(Case(When(status__isnull=True, then=1), default=None, output_field=FloatField()))
        )['successful_pos']

        return (successful_pos / total_pos) * 100



class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.po_number} - {self.vendor.name}"
    

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"