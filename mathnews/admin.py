from django.contrib import admin
from mathnews.models import TechNews, Like
from django.contrib.auth.models import User, Group


class TechNewsAdmin(admin.ModelAdmin):
  list_display= ["heading", "part_1", "part_2", 'author', "timeline", "validate"]


admin.site.register(TechNews, TechNewsAdmin)
admin.site.register(Like)




admin.site.unregister(Group)