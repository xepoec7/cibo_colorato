from django.forms import ModelForm, Textarea
from .models import Rechnung

class RechnungForm(ModelForm):
	class Meta:
		model = Rechnung
		fields = ['bestellt_per', 'kunden_name', 'kunden_tel', 'notiz', ]
		widgets = {
			'notiz': Textarea(attrs={'cols': 10, 'rows': 3}),
		}