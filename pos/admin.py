from django.contrib import admin
from .models import *

@admin.register(Kategorie)
class KategorieAdmin(admin.ModelAdmin):
	pass


@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    '''
        Admin View for Artikel
    '''
    list_display = ('kategorie', 'name', 'preis', 'auf_karte',)
    list_filter = ('kategorie', 'auf_karte', )
    search_fields = ('name',)


@admin.register(Rechnung)
class RechnungAdmin(admin.ModelAdmin):
	list_display = ('benutzer', 'erstellt', 'bestellt_per', 'kunden_name', 'total', 'ausgedruckt',)
	list_filter = ('bestellt_per', 'ausgedruckt', )
	search_fields = ('kunden_name', )