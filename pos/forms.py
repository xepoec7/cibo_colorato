from django.forms import ModelForm
from .models import Rechnung

class RechnungForm(ModelForm):
	class Meta:
		model = Rechnung
		fields = ['bestellt_per', 'kunden_name', 'kunden_tel', ]