from django.contrib import admin
from mathnews.models import TechNews
from django.contrib.auth.models import User, Group


class TechNewsAdmin(admin.ModelAdmin):
  list_display= ["heading", "paragraph1", "paragraph2", 'author', "timeline", "validate"]


admin.site.register(TechNews, TechNewsAdmin)

admin.site.unregister(Group)