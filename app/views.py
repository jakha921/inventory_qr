from django.shortcuts import render

from app.models import Room
from app.utils import create_qrcode


# Create your views here.
def index(request, room_id):
    room = Room.objects.get(id=room_id)
    teacher = room.teacher_set.all()[0]
    invernments = room.roominventory_set.all()
    sum_invernments = sum([invernment.count for invernment in invernments])

    context = {
        'room': room,
        'teacher': teacher,
        'invernments': invernments,
        'sum_invernments': sum_invernments
    }

    return render(request, "app/index.html", context)


def internment(request):
    rooms = Room.objects.all()

    # generate_qrcode('path', 'name', 'link')
    # set path

    # for room in rooms:
    #     url = f'http://213.230.69.57:8888/invernment/room/{room.id}'
    #     create_qrcode(url, room.room_number)

    context = {
        'rooms': rooms
    }
    return render(request, "app/invernments.html", context)


# def warehouse_details(request):
#     warehouse = Warehouse.objects.all().order_by('inventory__name', 'price')
#
#     # add new var to warehouse
#     for item in warehouse:
#         item.total_price = item.count * item.price
#
#     sum_price = sum([item.total_price for item in warehouse])
#
#     return render(request, "app/warehouse.html", {'warehouses': warehouse, 'sum_price': sum_price})
