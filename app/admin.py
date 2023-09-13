from django.contrib import admin

from app.models import Corpus, Floor, Room, Teacher, Inventory, RoomInventory

# Register your models here.
admin.site.site_header = 'Inventar boshqaruv tizimi'
admin.site.site_title = 'Inventar boshqaruv tizimi'
admin.site.index_title = 'Inventar boshqaruv tizimi'


@admin.register(Corpus)
class CorpusAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description')
    list_filter = ('name', 'address')
    search_fields = ('name', 'address', 'description')
    list_display_links = ('name',)
    list_editable = ('address',)


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('floor_locations', 'floor_number', 'corpus')
    list_filter = ('floor_number', 'corpus')
    search_fields = ('floor_number', 'corpus')
    list_editable = ('floor_number', 'corpus')

    def floor_locations(self, obj):
        """return as list number and name"""
        return f'{obj.corpus.name} Korpusi, {obj.floor_number} - qavat'

    floor_locations.short_description = 'Qavat joylashgan joyi'


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_locations', 'floor', 'room_number')
    list_filter = ('room_number', 'floor')
    search_fields = ('room_number', 'floor')
    list_editable = ('room_number', 'floor')

    def room_locations(self, obj):
        """return as list number and name"""
        return f'{obj.floor.corpus.name} Korpusi, {obj.floor.floor_number} - qavat, {obj.room_number} - xona'

    room_locations.short_description = 'Xona joylashgan joyi'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_room', 'name', 'surname', 'patronymic', 'phone', 'email', 'room')
    list_filter = ('name', 'surname', 'patronymic', 'phone', 'email', 'room')
    search_fields = ('name', 'surname', 'patronymic', 'phone', 'email', 'room')
    list_editable = ('name', 'surname', 'patronymic', 'phone', 'email', 'room')

    def teacher_room(self, obj):
        return (f'{obj.room.floor.corpus.name} Korpusi, {obj.room.floor.floor_number} - qavat, '
                f'{obj.room.room_number} - xona, {obj.surname} {obj.name} {obj.patronymic or ""}')

    teacher_room.short_description = 'O`qituvchiga tegishli xona'


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('invetory_name', 'name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    list_editable = ('name',)

    def invetory_name(self, obj):
        return f'{obj.name} {obj.description or ""}'

    invetory_name.short_description = 'Inventar nomi'


@admin.register(RoomInventory)
class RoomInventoryAdmin(admin.ModelAdmin):
    list_display = ('inverntor_room', 'room', 'inventory', 'count')
    list_filter = ('room', 'inventory', 'count')
    search_fields = ('room', 'inventory', 'count')
    list_editable = ('room', 'inventory', 'count')

    def inverntor_room(self, obj):
        return f'{obj.room} xonasida {obj.inventory} {obj.count} ta mavjud'

    inverntor_room.short_description = 'Inventar xonada mavjudligi'
