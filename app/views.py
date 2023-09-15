from django.shortcuts import render
from django.http import HttpResponse

from app.models import Room


# Create your views here.
def index(request, room_id):
    room = Room.objects.get(id=room_id)
    teacher = room.teacher_set.all()[0]
    invernments = room.roominventory_set.all()
    index = [i for i in range(1, len(invernments) + 1)]

    context = {
        'room': room,
        'teacher': teacher,
        'invernments': invernments,
        'index': index
    }

    return render(request, "app/index.html", context)
