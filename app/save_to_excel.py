import openpyxl
from django.http import HttpResponse


def export_room_inventory_to_excel(modeladmin, request, queryset):
    # Create an in-memory workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Room Inventory'

    # Add header row
    headers = ['Xona', 'Inventar', 'Inventar raqami']
    sheet.append(headers)

    # Add data rows
    for room in queryset:
        for room_inventory in room.roominventory_set.all():
            row = [
                room_inventory.room.room_number,
                room_inventory.inventory.name,
                room_inventory.inventory_number,
            ]
            sheet.append(row)

    # Set the response as an Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={queryset.first().room_number}_inventory.xlsx'
    workbook.save(response)
    return response


export_room_inventory_to_excel.short_description = "Excel-ga tanlangan xonani inventarlarini yuklash"


def export_employee_inventory_to_excel(modeladmin, request, queryset):
    # Create an in-memory workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Employee Inventory'

    # Add header row
    headers = ['Xodim', 'Inventar', 'Inventar raqami']
    sheet.append(headers)

    # Add data rows
    for employee in queryset:
        for employee_inventory in employee.employeeinventory_set.all():
            row = [
                employee_inventory.employee.surname + ' ' + employee_inventory.employee.name,
                employee_inventory.inventory.name,
                employee_inventory.inventory_number,
            ]
            sheet.append(row)

    # Set the response as an Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={queryset.first().surname}_{queryset.first().name}_inventory.xlsx'
    workbook.save(response)
    return response


export_employee_inventory_to_excel.short_description = "Excel-ga tanlangan xodim inventarlarini yuklash"