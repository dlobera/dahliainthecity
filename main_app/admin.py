from django.contrib import admin
# import your models here
from .models import Place, Visit

# Register your models here
admin.site.register(Place)
admin.site.register(Visit)