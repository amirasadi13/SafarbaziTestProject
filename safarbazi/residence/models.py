from django.db import models
from safarbazi.common.models import BaseModel, Province, City


class Residence(BaseModel):
    title = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    latitude = models.CharField(max_length=50, blank=True)
    longitude = models.CharField(max_length=50, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['title', ]),
            models.Index(fields=['province', ]),
        ]

    def __str__(self):
        return self.title


class Room(BaseModel):
    title = models.CharField(max_length=150)
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    base_guests_count = models.PositiveIntegerField(default=1)
    max_guests_count = models.PositiveIntegerField(default=0)
    adult_extra_price = models.PositiveIntegerField(default=0)
    child_extra_price = models.PositiveIntegerField(default=0)
    baby_extra_price = models.PositiveIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['residence', ]),
        ]

    def __str__(self):
        return self.title


class Calendar(BaseModel):
    room = models.OneToOneField(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.room.title

    class Meta:
        indexes = [
            models.Index(fields=['room', ]),
        ]


class Date(BaseModel):
    STATUS = (
        ('empty', 'empty'),
        ('booked', 'booked')
    )
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    date = models.DateField()
    base_amount = models.PositiveIntegerField(blank=True, null=True)
    adult_extra_amount = models.PositiveIntegerField(blank=True, null=True)
    child_extra_amount = models.PositiveIntegerField(blank=True, null=True)
    baby_extra_amount = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='empty')

    class Meta:
        unique_together = ('calendar', 'date',)
        indexes = [
            models.Index(fields=['date', 'calendar', 'status']),
        ]
