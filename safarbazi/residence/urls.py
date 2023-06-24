from django.urls import path

from safarbazi.residence.apis.calendar import CalendarApi
from safarbazi.residence.apis.check_prices import CheckPricesApi
from safarbazi.residence.apis.residence import ResidenceApi
from safarbazi.residence.apis.room import RoomApi

urlpatterns = [
    path('residence/', ResidenceApi.as_view(), name='residence'),
    path('room/', RoomApi.as_view(), name='room'),
    path('calendar/', CalendarApi.as_view(), name='calendar'),
    path('check/', CheckPricesApi.as_view(), name='check'),
]