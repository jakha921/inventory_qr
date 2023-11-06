from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

from app.models import Warehouse, RoomInventory, TeacherInventory


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
                    price=instance.price
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


# Signal executed after saving a RoomInventory object and TeacherInventory object
@receiver(post_save, sender=RoomInventory)
@receiver(post_save, sender=TeacherInventory)
def update_warehouse_count(sender, instance, **kwargs):
    # Get the current count in the 'Omborda' record for the given inventory
    try:
        warehouse = Warehouse.objects.get(inventory=instance.inventory, status='Omborda')
    except Warehouse.DoesNotExist:
        raise Exception("Ushbu inventar omborida mavjud emas.")

    if warehouse:
        # Calculate the difference between the previous count and the new count
        if instance.pk is not None:
            old_instance = sender.objects.get(pk=instance.pk)
            count_difference = instance.count - old_instance.count
        else:
            count_difference = instance.count

        # Check if the count difference is valid
        if warehouse.count - count_difference >= 0:
            # Update the warehouse count
            warehouse.count -= count_difference
            warehouse.save()
        else:
            # Rollback the count update
            raise Exception('Omborda inventarizatsiya etarli emas')


@receiver(pre_delete, sender=RoomInventory)
@receiver(pre_delete, sender=TeacherInventory)
def update_warehouse_count_on_delete(sender, instance, **kwargs):
    # Get the current count in the 'Omborda' record for the given inventory
    try:
        warehouse = Warehouse.objects.get(inventory=instance.inventory, status='Omborda')
    except Warehouse.DoesNotExist:
        raise Exception("Ushbu inventar omborida mavjud emas.")

    if warehouse:
        # Increase the warehouse count when a record is deleted
        warehouse.count += instance.count
        warehouse.save()
