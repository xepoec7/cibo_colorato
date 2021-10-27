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
    list_display = ('name', 'kategorie', 'preis', 'auf_karte',)
    list_filter = ('kategorie', 'auf_karte', )
    search_fields = ('name',)


class EinheitInline(admin.TabularInline):
    model = Einheit
    extra = 0


@admin.register(Rechnung)
class RechnungAdmin(admin.ModelAdmin):
    inlines = [EinheitInline, ]
    list_display = ('rechnung_num', 'erstellt', 'bestellt_per', 'kunden_name', 'total', 'ausgedruckt')
    list_filter = ('bestellt_per', 'ausgedruckt')
    search_fields = ('kunden_name', 'rechnung_num',)


@admin.register(Nachricht)
class NachrichtAdmin(admin.ModelAdmin):
    list_display = ('von', 'erstellt', 'ausgedruckt',)


@admin.register(KioskSeite)
class KioskSeiteAdmin(admin.ModelAdmin):
    list_display = ('bild', 'aktiv',)