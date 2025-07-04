from django.contrib import admin  # NOQA: F401

from accounts.models import Gamer

admin.site.register([Gamer])
