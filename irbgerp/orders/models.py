from django.db import models
from django.conf import settings

class Order(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=255)
    platform = models.CharField(max_length=100)
    expected_start_date = models.DateField()
    expected_end_date = models.DateField()
    order_amount_ex_vat = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_vat = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='artist_orders')
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='manager_orders')
    attachment = models.FileField(upload_to='attachments/')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_number
