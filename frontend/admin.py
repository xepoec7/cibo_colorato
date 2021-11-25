from django.contrib import admin
from .models import *


@admin.register(Einstellung)
class EinstellungAdmin(admin.ModelAdmin):
	pass



@admin.register(BilderGalerie)
class BilderGalerieAdmin(admin.ModelAdmin):
	pass


@admin.register(Aktion)
class AktionAdmin(admin.ModelAdmin):
	pass



@admin.register(LieferungService)
class LieferungServiceAdmin(admin.ModelAdmin):
	pass