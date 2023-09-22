from django.db import models


# Create your models here.
# Create models as Corpus, Floor, Room, Teacher, Invetory, RoomInventory

class Corpus(models.Model):
    name = models.CharField('Korpus nomi', max_length=255)
    address = models.CharField('Korpus manzili', max_length=100, blank=True, null=True)
    description = models.TextField('Korpus haqida malumot', blank=True, null=True)

    def __str__(self):
        return f"Corpus: {self.name}"

    class Meta:
        verbose_name_plural = 'Korpus'
        verbose_name = 'Korpuslar'


class Floor(models.Model):
    floor_number = models.IntegerField('Qavat raqami')
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE, verbose_name='Korpus')

    def __str__(self):
        return f"Floors: {self.floor_number} - {self.corpus.name}"

    class Meta:
        verbose_name_plural = 'Qavat'
        verbose_name = 'Qavatlar'


class Room(models.Model):
    room_number = models.CharField('Xona raqami', max_length=255)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, verbose_name='Qavat')

    def __str__(self):
        return f"Room: {self.room_number} - {self.floor.floor_number}"

    class Meta:
        verbose_name_plural = 'Xona'
        verbose_name = 'Xonalar'


class Teacher(models.Model):
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
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Ma`sul xona')
    degree = models.CharField('Ilmiy darajasi', max_length=255, choices=degree_choices, default='O`rta', blank=True,
                              null=True)
    description = models.TextField('Qisqacha ma`lumot', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Rasm')

    def __str__(self):
        return f"Teacher: {self.name} {self.surname} - {self.room}"

    class Meta:
        verbose_name_plural = 'Ma`sul'
        verbose_name = 'Ma`sullar'


class Inventory(models.Model):
    name = models.CharField('Inventar nomi', max_length=255)  # 'Inventar nomi
    description = models.TextField('Inventar haqida malumot', blank=True, null=True)  # 'Inventar haqida malumot
    photo = models.ImageField(upload_to='inventories/', blank=True, null=True, verbose_name='Inventar rasmi')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Inventar'
        verbose_name = 'Inventarlar'


class RoomInventory(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Xona raqami')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name='Inventar nomi')
    count = models.IntegerField('Soni')

    def __str__(self):
        return f'Resurs: {self.inventory.name} - {self.room.room_number}'

    class Meta:
        verbose_name_plural = 'Xonadagi inventar'
        verbose_name = 'Xonadagi inventarlar'


class Warehouse(models.Model):
    status_choices = (
        ('Omborda', 'Omborda'),
        ('Ta`mir qilinmoqda', 'Ta`mir qilinmoqda'),
        ('Xonaga o`rnatilgan', 'Xonaga o`rnatilgan'),
        ('Buzilgan', 'Buzilgan'),
    )

    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name='Inventar nomi')
    count = models.IntegerField('Soni')
    status = models.CharField('Holati', max_length=255, choices=status_choices, default='Omborda')

    def __str__(self):
        return f'Inventar: {self.inventory.name}'

    class Meta:
        verbose_name_plural = 'Ombor'
        verbose_name = 'Omborlar'
