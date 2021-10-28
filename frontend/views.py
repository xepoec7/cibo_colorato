from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from pos.models import Kategorie, Artikel, KioskSeite


def home_page(request):
	return render(request, 'home.html', {})


def kiosk_page(request):
	kiosk = KioskSeite.objects.all()
	return render(request, 'kiosk.html', {'kiosk': kiosk})


def menu_page(request):
	kats = Kategorie.objects.all()
	arts = Artikel.objects.order_by('-kategorie')
	contx = {'kategorien': kats, 'artikeln': arts}
	return render(request, 'menu.html', contx)



# AJAX 
def ajax_menu_nav(request, cat_id):
	if cat_id == 0:
		arts = Artikel.objects.all(auf_karte=True)
	else:
		kat = Kategorie.objects.get(pk=cat_id)
		arts = Artikel.objects.all().filter(kategorie=kat)
	#arts = serializers.serialize('json', arts)
	resp = {'artikeln': arts}
	return JsonResponse(resp, safe=False)