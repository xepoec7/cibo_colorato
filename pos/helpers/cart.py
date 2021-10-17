from decimal import Decimal
from django.conf import settings
from ..models import Artikel

class Cart(object):

	def __init__(self, request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart


	def add(self, product, qty=1, override_qty=False):
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'qty': 0, 'price': str(product.preis)}

		if override_qty:
			self.cart[product_id]['qty'] += qty
		else:
			self.cart[product_id]['qty'] += qty
		self.save()


	def save(self):
		self.session.modified = True


	def remove(self, product):
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()


	def __iter__(self):
		product_ids = self.cart.keys()
		products = Artikel.objects.filter(id__in=product_ids)

		cart = self.cart.copy()
		for product in products:
			cart[str(product.id)]['product'] = product

		for item in cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['qty']
			yield item


	
	def __len__(self):
		return sum(item['qty'] for item in self.cart.values())



	def get_total_price(self):
		total = 0
		for item in self.cart.values():
			x = Decimal(item['price']) * Decimal(item['qty'])
			total += x
		return total



	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.save()
