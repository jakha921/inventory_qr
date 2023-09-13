from django.db import models


# Create your models here.
# Create models as Corpus, Floor, Room, Teacher, Invetory, RoomInventory

class Corpus(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Korpus'
        verbose_name = 'Korpuslar'


class Floor(models.Model):
    floor_number = models.IntegerField()
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.corpus.name} - {self.floor_number}'

    class Meta:
        verbose_name_plural = 'Qavat'
        verbose_name = 'Qavatlar'


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.floor.corpus.name} - {self.floor.floor_number} - {self.room_number}'

    class Meta:
        verbose_name_plural = 'Xona'
        verbose_name = 'Xonalar'


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.CharField(max_length=255,
                             default='https://www.citypng.com/public/uploads/preview/black-user-member-guest-icon-31634946589seopngzc1t.png')
    email = models.EmailField(blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.surname} {self.name} -> {self.room}'

    class Meta:
        verbose_name_plural = 'O`qituvchi'
        verbose_name = 'O`qituvchilar'


class Inventory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Inventar'
        verbose_name = 'Inventarlar'


class RoomInventory(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.room} - {self.inventory} - {self.count}'

    class Meta:
        verbose_name_plural = 'Xonadagi inventar'
        verbose_name = 'Xonadagi inventarlar'
