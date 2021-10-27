from django.shortcuts import render
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