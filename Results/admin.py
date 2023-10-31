from django.contrib import admin

from .models import States, LGA, Ward, PollingUnit, AnnouncedPuResults, AnnouncedLgaResults

admin.site.register(States)
admin.site.register(LGA)
admin.site.register(Ward)
admin.site.register(PollingUnit)
admin.site.register(AnnouncedPuResults)
admin.site.register(AnnouncedLgaResults)

