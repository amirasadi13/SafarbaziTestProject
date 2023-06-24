from django.contrib import admin

from safarbazi.residence.models import Residence, Room, Calendar, Date

admin.site.register(Residence)
admin.site.register(Room)
admin.site.register(Calendar)
admin.site.register(Date)
