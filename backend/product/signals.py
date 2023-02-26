
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product
from django_q.models import Schedule

@receiver(pre_save, sender=Product)
def save_or_change_product(sender, instance, **kwargs):
    # print("yes printing...")
    # print(instance.id, instance.website, instance.url)
    func_data = {
        "website": instance.website,
        "url": instance.url
    }
    if instance.id is not None:
        schedule = Schedule.objects.get(pk=instance.schedule_id)
        schedule.kwargs=func_data
        schedule.save()
    else:
        print(instance.id, instance.website)
        schedule = Schedule.objects.create(
            name=f"schedule-product-{instance.id}",
            func="product.util.get_price",
            kwargs=func_data,
            schedule_type=Schedule.MINUTES,
            minutes=1,
            repeats=-1,
        )
        instance.schedule_id = schedule.id