from django.db import models
from django.conf import settings

class Kategorie(models.Model):
	name = models.CharField(max_length=30)
	bild = models.ImageField(upload_to="kat_bilder", blank=True, null=True)

	def __str__(self):
		return self.name



class Artikel(models.Model):
	kategorie = models.ForeignKey(Kategorie, null=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=30)
	bild = models.ImageField(upload_to="artikel_bilder", blank=True, null=True)
	preis = models.DecimalField(max_digits=7, decimal_places=2)
	auf_karte = models.BooleanField(default=True, blank=True)
	zutaten = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name



class MeistGekaufte(models.Model):
	artikel_1 = models.ForeignKey(Artikel, null=True, blank=True, on_delete=models.SET_NULL, related_name='artikel_1')
	artikel_2 = models.ForeignKey(Artikel, null=True, blank=True, on_delete=models.SET_NULL, related_name='artikel_2')
	artikel_3 = models.ForeignKey(Artikel, null=True, blank=True, on_delete=models.SET_NULL, related_name='artikel_3')
	artikel_4 = models.ForeignKey(Artikel, null=True, blank=True, on_delete=models.SET_NULL, related_name='artikel_4')

	def __str__(self):
		return 'Liste von 4 Artikeln'



class Rechnung(models.Model):
	BESTELT_PER = (
		("TEL", "Telefonisch"),
		('ONLINE', 'Online'),
		('DIREKT', 'Direkt'),
	)
	benutzer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
	rechnung_num = models.CharField(max_length=7, null=True)
	erstellt = models.DateTimeField(auto_now_add=True, blank=True)
	bestellt_per = models.CharField(max_length=15, choices=BESTELT_PER, default='TEL')
	kunden_name = models.CharField(max_length=30, blank=True, null=True)
	kunden_tel = models.CharField(max_length=10, blank=True, null=True)
	notiz = models.CharField(max_length=100, blank=True, null=True)
	total = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.00)
	ausgedruckt = models.BooleanField(default=False, blank=True)

	def __str__(self):
		return self.rechnung_num



class Einheit(models.Model):
	rechnung = models.ForeignKey(Rechnung, on_delete=models.CASCADE)
	artikel = models.ForeignKey(Artikel, null=True, on_delete=models.SET_NULL)
	mange = models.IntegerField()



class Nachricht(models.Model):
	von = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
	erstellt = models.DateTimeField(auto_now_add=True, blank=True)
	ausgedruckt = models.BooleanField(default=False, blank=True)
	nachricht = models.CharField(max_length=100)



class KioskSeite(models.Model):
	bild = models.ImageField(upload_to="kiosk")
	aktiv = models.BooleanField(default=True, blank=True)