
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from django_q.models import Schedule
import datetime
from django.utils import timezone

@receiver(post_save, sender=Product)
def save_or_change_product(sender, instance, **kwargs):
    # print("yes printing...")
    # print(f"Instance id=>{instance.id}")
    # print(instance.id, instance.website, instance.url)
    func_data = {
        "product_id": instance.id,
        "website": instance.website,
        "url": instance.url
    }
    if instance.schedule_id:
        schedule = Schedule.objects.get(pk=instance.schedule_id)
        schedule.kwargs=func_data
        schedule.save()
    else:
        schedule = Schedule.objects.create(
            name=f"schedule-{instance.name[:20]}",
            func="product.util.get_price",
            kwargs=func_data,
            schedule_type=Schedule.MINUTES,
            minutes=120,
            repeats=-1,
            next_run=timezone.now() + datetime.timedelta(seconds=10)
        )
        instance.schedule_id = schedule.id
        instance.save()