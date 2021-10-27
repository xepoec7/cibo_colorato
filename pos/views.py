import json
from decimal import Decimal

from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Kategorie, Artikel, Rechnung, Einheit, Nachricht
from .helpers.cart import Cart
from .helpers.printer import Printer
from .forms import RechnungForm


@login_required
def pos_page(request):
	items = Kategorie.objects.all()
	return render(request, 'pos.html', {'items': items})



@login_required
def pos_check(request):
	cart = Cart(request)

	if request.method == 'POST':
		form = RechnungForm(request.POST)
		if form.is_valid():
			rechn_num = ""
			invs = Rechnung.objects.all()
			if len(invs) is 0:
				rechn_num = "CC1000"
			else:
				invs = Rechnung.objects.all().last()
				s = int(invs.rechnung_num[2:]) + 1 
				rechn_num = "CC" + str(s)

			rechnung = form.save()
			rechnung.benutzer = request.user
			rechnung.total = cart.get_total_price()
			rechnung.rechnung_num = rechn_num
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




@login_required
def pos_sent(request):
	return render(request, 'order_sent.html', {})




@login_required
def pos_msg(request):
	if request.method == 'POST':
		msg = request.POST['msg_f']
		nachricht = Nachricht(von=request.user, nachricht=msg)
		printer = Printer()
		printer.print_msg(request.user.username, msg)
		nachricht.ausgedruckt = True
		nachricht.save()
	return render(request, 'msg.html', {})





""" AJAX FUNCTIONS """
@login_required
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

@login_required
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

@login_required
def cart_remove(request, id):
	product = Artikel.objects.get(id=id)
	cart = Cart(request)
	cart.remove(product)
	return JsonResponse({'response': 'OK'})