from django.contrib import admin
from django.utils.safestring import mark_safe

from app.models import Corpus, Floor, Room, Teacher, Inventory, RoomInventory, Warehouse, TeacherInventory, \
    AdditionalExpense, AdditionalExpensePhoto

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
        return f'ID: {obj.id}, {obj.floor.corpus.name} Korpusi, {obj.floor.floor_number} - qavat, {obj.room_number} - xona'

    room_locations.short_description = 'Xona joylashgan joyi'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_room', 'name', 'surname', 'patronymic', 'room')
    list_filter = ('name', 'surname', 'room')
    search_fields = ('name', 'surname', 'patronymic', 'phone', 'email', 'room')
    list_editable = ('name', 'surname', 'patronymic', 'room')

    def teacher_room(self, obj):
        msg = f'{obj.surname} {obj.name} {obj.patronymic or ""}'
        if obj.room:
            msg += f' - {obj.room.room_number} - xona'
        return msg

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


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('inventory_name', 'inventory', 'status', 'count')
    list_filter = ('status', 'inventory')
    search_fields = ('inventory', 'status', 'count')
    list_editable = ('count',)

    # readonly_fields = ('inventory', 'status')

    def inventory_name(self, obj):
        return f'{obj.inventory.name} {obj.count} ta' if obj.inventory else f'{obj.id} - {obj.count} ta'

    inventory_name.short_description = 'Inventar'


@admin.register(TeacherInventory)
class TeacherInventoryAdmin(admin.ModelAdmin):
    list_display = ('teacher_inventory', 'teacher', 'inventory', 'count')
    list_filter = ('teacher', 'inventory', 'count')
    search_fields = ('teacher', 'inventory', 'count')
    list_editable = ('count',)

    def teacher_inventory(self, obj):
        return f"{obj.teacher.surname} {obj.teacher.name} - {obj.inventory.name}"

    teacher_inventory.short_description = 'O`qituvchi inventari'


# register additional expense photo inline
class AdditionalExpensePhotoInline(admin.TabularInline):
    model = AdditionalExpensePhoto
    extra = 1
    fields = ('photo', 'photo_preview')
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="200" height="150" />')
        return 'Rasm yo`q'

    photo_preview.short_description = 'Rasm'


@admin.register(AdditionalExpense)
class AdditionalExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'action_date', 'check_img_preview')
    list_filter = ('name', 'price', 'action_date')
    search_fields = ('name', 'price', 'action_date')
    list_editable = ('price', 'action_date')

    # img preview
    readonly_fields = ('check_img_preview',)

    def check_img_preview(self, obj):
        if obj.check_img:
            return mark_safe(f'<img src="{obj.check_img.url}" width="100" height="70" />')
        return 'Rasm yo`q'

    check_img_preview.short_description = 'Chek rasmi'

    inlines = [AdditionalExpensePhotoInline]
