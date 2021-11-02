from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from pos.models import Kategorie, Artikel, KioskSeite, MeistGekaufte


def home_page(request):
	return render(request, 'home.html', {})


def kiosk_page(request):
	kiosk = KioskSeite.objects.all()
	return render(request, 'kiosk.html', {'kiosk': kiosk})


def menu_page(request):
	kats = Kategorie.objects.all()
	arts = Artikel.objects.order_by('-kategorie')
	popular = MeistGekaufte.objects.get(pk=1)
	contx = {'kategorien': kats, 'artikeln': arts, 'popular': popular}
	return render(request, 'menu.html', contx)



# AJAX 
def ajax_menu_nav(request, cat_id):
	art_list = []
	if cat_id == 0:
		resp = serializers.serialize('json', Artikel.objects.all())
	else:
		kat = Kategorie.objects.get(pk=cat_id)
		resp = serializers.serialize('json', kat.artikel_set.all())
	return HttpResponse(resp, content_type='application/json')