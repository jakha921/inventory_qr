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
@receiver(post_save, sender=Warehouse)
def update_omborda_count(sender, instance, **kwargs):
    try:
        old_instance = Warehouse.objects.get(pk=instance.pk)
    except Warehouse.DoesNotExist:
        old_instance = None

    if old_instance:
        if instance.status != 'Omborda':
            print('update_omborda_count ')
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
        warehouse_room = Warehouse.objects.get(inventory=instance.inventory, status='Xonaga o`rnatilgan')
    except Warehouse.DoesNotExist:
        raise Exception("Ushbu inventar omborida mavjud emas.")

    if warehouse:
        # Check if the record is being created or updated
        if kwargs['created']:
            # Decrease the warehouse count when a record is created
            warehouse.count -= instance.count
            warehouse_room.count += instance.count
        elif not kwargs['created']:
            # Calculate the difference in count between the current and old record
            count_diff = instance.count - instance.__class__.objects.get(pk=instance.pk).count

            # Update the warehouse count based on the change
            warehouse.count -= count_diff
            warehouse_room.count += count_diff

        warehouse.save()
        warehouse_room.save()


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
