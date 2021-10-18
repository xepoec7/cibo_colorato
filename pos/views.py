import json
from decimal import Decimal

from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from .models import Kategorie, Artikel, Rechnung, Einheit
from .helpers.cart import Cart
from .helpers.printer import Printer
from .forms import RechnungForm


def pos_page(request):
	items = Kategorie.objects.all()
	return render(request, 'pos.html', {'items': items})


def pos_check(request):
	cart = Cart(request)

	if request.method == 'POST':
		form = RechnungForm(request.POST)
		if form.is_valid():
			rechnung = form.save()
			rechnung.total = cart.get_total_price()
			rechnung.save()
			for item in cart:
				product = item['product']
				inv_item = Einheit(rechnung=rechnung, artikel=product, mange=item['qty'])
				inv_item.save()
			printer = Printer()
			is_printed = False
			while(is_printed == False):
				is_printed = printer.print_inv(rechnung)
			cart.clear()
			return redirect('pos:pos_sent')

	contx = {'cart': cart, 'form': RechnungForm()}
	return render(request, 'check.html', contx)


def pos_sent(request):
	return render(request, 'order_sent.html', {})


def pos_ajax(request, type=None, id=None, qty=1):
	items = None
	if type is None:
		items = serializers.serialize('json', Kategorie.objects.all())
	if type == 'pos.kategorie':
		kategorie = Kategorie.objects.get(id=id)
		items = serializers.serialize('json', kategorie.artikel_set.all())
	if type == 'pos.artikel':
		items = serializers.serialize('json', Kategorie.objects.all())
		product = Artikel.objects.get(id=id)
		override = False
		if qty > 1 : 
			override = True
		cart = Cart(request)
		cart.add(product, qty, override)

	return HttpResponse(items, content_type='application/json')


def cart_ajax(request):
	cart = Cart(request)
	cart_total = Decimal(cart.get_total_price())
	records = []

	for item in cart:
		product = item['product']
		item = {'id': product.id, 'name': product.name, 'qty': item['qty']}
		records.append(item)

	cart_total = str(cart_total)
	respond = {'cart_total': cart_total, 'items': records}
	#respond = json.dumps(respond)

	#return HttpResponse(respond, content_type='application/json')
	return JsonResponse(respond)


def cart_remove(request, id):
	product = Artikel.objects.get(id=id)
	cart = Cart(request)
	cart.remove(product)
	return JsonResponse({'response': 'OK'})