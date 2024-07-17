from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from app.models import Corpus, Room, Inventory, RoomInventory, EmployeeInventory, Employee
from app.save_to_excel import export_room_inventory_to_excel, export_employee_inventory_to_excel

# Register your models here.
admin.site.site_header = 'Inventar boshqaruv tizimi'
admin.site.site_title = 'Inventar boshqaruv tizimi'
admin.site.index_title = 'Inventar boshqaruv tizimi'


@admin.register(Corpus)
class CorpusAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description')
    search_fields = ('name', 'address', 'description')
    list_display_links = ('name',)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('invetory_name', 'name', 'description', 'price', 'count', 'image_preview')
    search_fields = ('name', 'description')

    def invetory_name(self, obj):
        return f'{obj.name} {obj.description or ""}'

    def image_preview(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width="85" height="55" />')
        return 'Rasm yo`q'

    invetory_name.short_description = 'Inventar nomi'
    image_preview.short_description = 'Rasm'


class RoomInventoryAdmin(admin.TabularInline):
    model = RoomInventory
    extra = 1
    can_delete = False
    classes = ('collapse',)
    show_change_link = True


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_locations', 'get_room_manager')
    list_filter = ('corpus',)  # 'room_number', 'room_manager'
    search_fields = (
        'room_number', 'room_manager__name', 'room_manager__surname', 'corpus__name', 'roominventory__inventory__name',
        'roominventory__inventory_number')
    actions = [export_room_inventory_to_excel]

    def room_locations(self, obj):
        """return as list number and name"""
        return f'ID: {obj.id}, {obj.corpus.name} > {obj.room_number}'

    room_locations.short_description = 'Xona joylashgan joyi'

    def get_room_manager(self, obj):
        # generate link to room manager
        if obj.room_manager:
            url = reverse('admin:app_employee_change', args=[obj.room_manager.id])
        return format_html('<a href="{}">{}</a>', url, obj.room_manager.surname + ' ' + obj.room_manager.name
                           ) if obj.room_manager else '-'

    get_room_manager.short_description = 'Xonaga masul xodim'

    inlines = [RoomInventoryAdmin]


class EmployeeInventoryAdmin(admin.TabularInline):
    model = EmployeeInventory
    extra = 1
    can_delete = False
    classes = ('collapse',)
    show_change_link = True


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'get_rooms')
    search_fields = (
        'name', 'surname', 'patronymic', 'phone', 'email', 'employeeinventory__inventory__name',
        'employeeinventory__inventory_number')
    actions = [export_employee_inventory_to_excel]

    inlines = [EmployeeInventoryAdmin]
