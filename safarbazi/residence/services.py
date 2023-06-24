from safarbazi.residence.models import Residence, Room, Calendar


def create_residence(*, title: str) -> Residence:
    return Residence.objects.create(title=title)


def create_room(*, title: str, residence: Residence) -> Room:
    room = Room.objects.create(title=title, residence=residence)
    get_or_create_calendar(room=room)
    return room


def get_or_create_calendar(*, room: Room) -> Calendar:
    try:
        return Calendar.objects.select_related("room").get(room=room)
    except Calendar.DoesNotExist:
        return Calendar.objects.create(room=room)
