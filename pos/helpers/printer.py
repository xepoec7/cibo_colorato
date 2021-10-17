from escpos import BluetoothConnection
from escpos.impl.epson import GenericESCPOS
from ..models import Rechnung


class Printer(object):
	"""
	Class to printing invoice on ESCPOS Printer.
	'''
	
	----------
	    rechnung : Rechnung
			       Rechnung model

		korb: Korb
		      Korb object in session

	Methods
	-------
	print_inv()
		Prints invoice and items in korb.

	print_msg(msg)
		Prints message

	set_inv_printed()
		Sets passed invoice as printed in database

	"""

	def __init__(self, inv="", cart=""):
		self.invoice = inv
		self.cart = cart
		self.printer = GenericESCPOS(BluetoothConnection('66:22:EC:FF:0D:CA'))


	def print_inv(self):
		# Method to print out cart and invoice data

		""" Company name in center with feed 3 above and 1 down """
		self.printer.lf(3)
		self.printer.set_text_size(1, 1) # Medium Font
		self-printer.text_center('Cibo Colorato')
		self.printer.lf(1)

		""" Invoice info """
		self.printer.set_text_size(0, 0) # Small font
		self.printer.justify_left() # Print from left
		out = 'Bestellnummer : {}'.format(self.invoice.id)
        self.printer.text(out)
        out = 'Datum         : {}'.format(self.invoice.erstellt.strftime('%d.%m.%Y %H:%M'))
        self.printer.text(out)
        out = 'Bestellung per: {}'.format(self.invoice.bestellt_per)
        self.printer.text(out)
        out = 'Auf Name      : {}'.format(self.invoice.kunden_name)
        self.printer.text(out)
        out = 'Tel Nummer    : {}'.format(self.invoice.kunden_tel)
        self.printer.text(out) 

        """ Items table """
        self.printer.text('ME Artikelname          EP  GP  ')
        self.printer.text('--------------------------------')

        """ Items """
        for item in self.cart:
            qty_and_name = '{}* {}'.format(item['qty'], item['product'])
            prices = '{} {}'.format(item['price'], item['total_price'])
            x = 33 - (len(prices) + 1) # Max char length in row - length of prices string
            out = f'{qty_and_name: <{x}}{prices}'
            self.printer.text(out)

        """ End of items table """
        self.printer.text('--------------------------------')

        """ Total sum of all items """
        self.printer.justify_right() # Print from right
        self.printer.set_text_size(1, 1) # Medium Font
        out = 'SUMME: {}'.format(self.cart.get_total_price())
        self.printer.text(out)
        self.printer.lf(4)

        print('\007') # Play beep
        self.set_inv_printed() # Mark invoice as printed
	


	def print_msg(self, user, msg):
		# Method for printing simple messages. 

		""" Header """
		self.printer.lf(3)
        self.printer.set_text_size(1, 1)
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


    def set_inv_printed(self):
    	# Method to mark invoice as printed
    	self.invoice.ausgedruckt = True
    	self.invoice.save()
