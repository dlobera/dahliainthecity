from django.contrib import admin
# import your models here
from .models import Place, Visit, Doing

# Register your models here
admin.site.register(Place)
admin.site.register(Visit)
admin.site.register(Doing)