from django.urls import path

from app.views import index, internment

urlpatterns = [
    path("", internment, name="internment"),
    path("invernment/room/<int:room_id>", index, name="index"),
]
