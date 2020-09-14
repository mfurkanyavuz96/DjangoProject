from django.contrib import admin
from .models import Vehicle, NavigationRecord, Bin, Operation, BinOperation

# Register your models here.

admin.site.register(Vehicle)
admin.site.register(NavigationRecord)
admin.site.register(Bin)
admin.site.register(Operation)
admin.site.register(BinOperation)
