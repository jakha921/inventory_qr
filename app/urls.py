from django.urls import path

from app.views import index

urlpatterns = [
    path("invernment/room/<int:room_id>", index, name="index"),
]
