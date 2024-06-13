from django.contrib import admin
from .models import PerevalAdded, User, Coord, Level, Image


class PerevalAddedAdmin(admin.ModelAdmin):
    model = PerevalAdded
    list_display = ('status', 'beauty_title', 'status', 'title', 'other_title', 'connect', 'user', 'coord', 'images')
    list_filter = ('add_time', 'beauty_title', 'title', 'other_title', 'user', 'level')


admin.site.register(PerevalAdded)
admin.site.register(User)
admin.site.register(Coord)
admin.site.register(Level)
admin.site.register(Image)