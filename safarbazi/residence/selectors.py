import uuid

from django.db.models import QuerySet, Sum, Value, F
from safarbazi.residence.models import Residence, Date, Room


def get_residence(*, residence_id: uuid.uuid4) -> Residence:
    return Residence.objects.get(id=residence_id)


def get_room(*, room_id: uuid.uuid4) -> Room:
    return Room.objects.get(id=room_id)


def get_calendar_available_dates(*, room: Room, checkin, checkout):
    dates = Date.objects.filter(calendar__room=room, date__range=[checkin, checkout], status='empty').order_by('date')
    if int((checkout - checkin).days + 1) > len(dates):
        return False
    return dates


def get_checked_dates_sum(available_dates: QuerySet[Date],
                          adult_count: int,
                          child_count: int,
                          baby_count: int) -> QuerySet[Date]:
    return available_dates \
        .annotate(adult_amount=Value(adult_count) * F('adult_extra_amount')) \
        .annotate(child_amount=Value(child_count) * F('child_extra_amount')) \
        .annotate(baby_amount=Value(baby_count) * F('baby_extra_amount')) \
        .aggregate(Sum(F('base_amount')),
                   Sum(F('adult_amount')),
                   Sum(F('child_amount')),
                   Sum(F('baby_amount'))
                   )


def get_or_create_date(*, date, room: Room, base_amount: int, adult_extra_amount: int,
                       child_extra_amount: int, baby_extra_amount: int, status: str) -> Date:
    current_date, created = Date.objects.get_or_create(calendar__room=room, date=date)
    current_date.base_amount = base_amount
    current_date.adult_extra_amount = adult_extra_amount
    current_date.child_extra_amount = child_extra_amount
    current_date.baby_extra_amount = baby_extra_amount
    current_date.status = status
    current_date.save()

    return current_date
