from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from app.models import Warehouse


# Signal executed after saving a Warehouse object
@receiver(post_save, sender=Warehouse)
def create_warehouse_statuses(sender, instance, **kwargs):
    if instance.status == 'Omborda':
        # Get available statuses except 'Omborda'
        status_choices = [choice[0] for choice in instance.status_choices if choice[0] != 'Omborda']
        for status in status_choices:
            # Check if there is no entry with the same inventory and status, and create a new one if not
            if not Warehouse.objects.filter(inventory=instance.inventory, status=status).exists():
                Warehouse.objects.create(
                    inventory=instance.inventory,
                    count=0,
                    status=status,
                )


# Signal executed before saving a Warehouse object
@receiver(pre_save, sender=Warehouse)
def update_omborda_count(sender, instance, **kwargs):
    try:
        old_instance = Warehouse.objects.get(pk=instance.pk)
    except Warehouse.DoesNotExist:
        old_instance = None

    if old_instance:
        if instance.status != 'Omborda':
            # Calculate the difference in count between the current and old record
            count_diff = instance.count - old_instance.count

            # Get the current count in the 'Omborda' record for the given inventory
            omborda_instance = Warehouse.objects.get(inventory=instance.inventory, status='Omborda')

            # Update the count in the 'Omborda' record based on the change
            omborda_instance.count -= count_diff
            omborda_instance.save()
