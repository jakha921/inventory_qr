from django.db import models
from django.urls import reverse
from django.utils.html import format_html


# Create your models here.
class Employee(models.Model):
    degree_choices = (
        ('O`rta', 'O`rta'),
        ('Bakalavr', 'Bakalavr'),
        ('Magistr', 'Magistr'),
        ('Doktorant', 'Doktorant'),
        ('Professor', 'Professor'),
        ('Akademik', 'Akademik'),
    )

    name = models.CharField('Ismi', max_length=255)  # 'Ismi
    surname = models.CharField('Familiyasi', max_length=255)  # 'Familiyasi
    patronymic = models.CharField('Otasining ismi', max_length=255, blank=True, null=True)  # 'Otasining ismi
    phone = models.CharField('Telefon raqami', max_length=255, blank=True, null=True)  # 'Telefon raqami
    image = models.CharField('Rasm', max_length=255,
                             default='https://cdn4.iconfinder.com/data/icons/signicon-pt-1-1/100/041_-_user_profile_avatar_login_account-1024.png')
    email = models.EmailField(blank=True, null=True)
    degree = models.CharField('Ilmiy darajasi', max_length=255, choices=degree_choices, default='O`rta', blank=True,
                              null=True)
    description = models.TextField('Qisqacha ma`lumot', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Rasm')

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Xodim: {self.name} {self.surname}"

    def get_rooms(self):
        rooms = self.room_set.all()
        room_links = []
        for room in rooms:
            url = reverse('admin:app_room_change', args=[room.id])
            room_links.append(format_html('<a href="{}">{}</a>', url, room.corpus.name + ' > ' + room.room_number))
        return format_html(', '.join(room_links))

    get_rooms.short_description = 'Xodim xonasi'

    class Meta:
        verbose_name_plural = 'Xodimlar'
        verbose_name = 'Xodimlar'
        ordering = ['surname', 'name']


class Corpus(models.Model):
    name = models.CharField('Korpus nomi', max_length=255)
    address = models.CharField('Korpus manzili', max_length=100, blank=True, null=True)
    description = models.TextField('Korpus haqida malumot', blank=True, null=True)

    def __str__(self):
        return f'Korpus: {self.name}'

    class Meta:
        verbose_name_plural = 'Korpus'
        verbose_name = 'Korpuslar'
        ordering = ['name']


class Room(models.Model):
    room_number = models.CharField('Xona raqami', max_length=255)
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE, verbose_name='Korpus')
    room_manager = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Xona masul xodim', blank=True,
                                     null=True)

    def __str__(self):
        return f"Korpus: {self.corpus.name} > Xona: {self.room_number}"

    class Meta:
        verbose_name_plural = 'Xona'
        verbose_name = 'Xonalar'
        ordering = ['room_number']


class Inventory(models.Model):
    name = models.CharField('Inventar nomi', max_length=255)  # 'Inventar nomi
    description = models.TextField('Inventar haqida malumot', blank=True, null=True)  # 'Inventar haqida malumot
    photo = models.ImageField(upload_to='inventories/', blank=True, null=True, verbose_name='Inventar rasmi')
    price = models.IntegerField('Inventar narxi', blank=True, null=True)  # 'Inventar narxi
    count = models.IntegerField('Invenrar soni', blank=True, null=True)  # 'Invenrar soni

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Inventar'
        verbose_name = 'Inventarlar'
        ordering = ['-created_at']


class RoomInventory(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Xona raqami')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name='Inventar nomi')
    inventory_number = models.CharField('Inventar raqami', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'Resurs: {self.inventory.name} - {self.room.room_number}'

    class Meta:
        verbose_name_plural = 'Xonadagi inventar'
        verbose_name = 'Xonadagi inventarlar'
        ordering = ['-created_at']


class EmployeeInventory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Xodim')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name='Inventar nomi')
    inventory_number = models.CharField('Inventar raqami', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.employee.name}: {self.inventory.name} - {self.inventory_number}"

    class Meta:
        verbose_name_plural = 'Xodimdagi inventar'
        verbose_name = 'Xodimlardagi inventarlar'
        ordering = ['-created_at']
