from escpos import BluetoothConnection
from escpos.impl.epson import GenericESCPOS
from ..models import Rechnung, Einheit


class Printer(object):

	def __init__(self):
		self.printer = GenericESCPOS(BluetoothConnection('66:22:EC:FF:0D:CA'))



	def print_inv(self, inv):
		try:
			inv_items = inv.einheit_set.all()

			self.printer.lf(3)
			self.printer.set_text_size(1, 1)
			self.printer.text_center('Cibo Colorato')
			self.printer.lf(1)

			self.printer.set_text_size(0, 0)
			self.printer.justify_left()
			out = 'Bestellnummer: {}'.format(inv.id)
			self.printer.text(out)
			out = 'Datum         : {}'.format(inv.erstellt.strftime('%d.%m.%Y %H:%M'))
			self.printer.text(out)
			out = 'Bestellung per: {}'.format(inv.bestellt_per)
			self.printer.text(out)
			out = 'Auf Name      : {}'.format(inv.kunden_name)
			self.printer.text(out)
			out = 'Tel Nummer    : {}'.format(inv.kunden_tel)
			self.printer.text(out)

			""" Items """ 
			self.printer.text('ME Artikelname          EP  GP  ')
			self.printer.text('--------------------------------')

			for item in inv_items:
				qty_and_name = '{}* {}'.format(item.mange, item.artikel.name)
				prices = '{} {}'.format(item.artikel.preis, item.mange * item.artikel.preis)
				x = 33 - (len(prices) +1) 
				out =f'{qty_and_name: <{x}}{prices}'
				self.printer.text(out)
			self.printer.text('--------------------------------')

			""" Total sum of all items """
			self.printer.justify_right()
			self.printer.set_text_size(1, 1)
			out = 'SUMME: {}'.format(inv.total)
			self.printer.text(out)
			self.printer.lf(4)

			print('\007')
			inv.ausgedruckt = True
			inv.save()

			return True

		except Exception as ex:
			print(ex)
			return False


	def print_msg(self, user, msg): 
		self.printer.lf(3)
		self.printer.set_text_size(1,1)
		self.printer.text_center('---------------')
		self.printer.text_center('!! NACHRICHT !!')
		self.printer.text_center('---------------')
		self.printer.lf(1)
		self.printer.set_text_size(0, 0)
		self.printer.justify_left()
		out = f'Von: {user}'
		self.printer.text(out)
		self.printer.lf(1)
		out = 'Nachricht:'
		self.printer.text(out)
		self.printer.text(msg)
		self.printer.lf(1)
		self.printer.text('--------------ende--------------')
		self.printer.lf(4)
		print('\007')