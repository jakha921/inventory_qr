from django.urls import path

from app.views import index, internment, warehouse_details

urlpatterns = [
    path("", internment, name="internment"),
    path("invernment/room/<int:room_id>", index, name="index"),
    path("warehouse/", warehouse_details, name="warehouse_details"),
]
