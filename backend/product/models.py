from django.db import models
from django_q.models import Schedule 

# Create your models here.
class Product(models.Model):

    AVAILABLE_CHOICES = [
        ('AMAZON', 'AMAZON'),
        ('MYNTRA', 'MYNTRA'),
    ]

    name = models.CharField(max_length = 1000, blank=False)
    url = models.URLField(max_length=500, unique=True, db_index=True)
    website = models.CharField(max_length=50, choices=AVAILABLE_CHOICES)
    schedule_id = models.BigIntegerField(default=0)

    def delete(self, *args, **kwargs):
        try:
            Schedule.objects.get(pk=self.schedule_id).delete()
        except:
            pass
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.website}-{self.name[:50]}"

class PriceData(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}-{self.price}"