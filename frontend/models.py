from django.db import models


class Einstellung(models.Model):
	TAGE = (
		('Mon', 'Montag'),
		('Die', 'Dienstag'),
		('Mit', 'Mittwoch'),
		('Don', 'Donnerstag'),
		('Fre', 'Freitag'),
		('Sam', 'Samstag'),
		('Son', 'Sonntag'),
	)
	email = models.CharField(max_length=60, blank=True, null=True)
	tel = models.CharField(max_length=12, blank=True, null=True)
	instagram = models.CharField(max_length=80, blank=True, null=True)
	facebook = models.CharField(max_length=80, blank=True, null=True)
	home_page_cover_bild = models.ImageField(upload_to="einstellung/cover", blank=True, null=True)
	uber_uns_text = models.TextField()
	uber_uns_bild = models.ImageField(upload_to="einstellung/cover", blank=True, null=True)
	offnungs_zeit_von = models.TimeField(blank=True, null=True)
	offnungs_zeit_bis = models.TimeField(blank=True, null=True)
	freier_tag = models.CharField(max_length=3, choices=TAGE, default='Mon', blank=True)


	class Meta:
		verbose_name = "Einstellung"
		verbose_name_plural = "Einstellung"

	def __str__(self):
		return 'Website Einstellung'


class BilderGalerie(models.Model):
	bild = models.ImageField(upload_to="einstellung/gallery")

	class Meta:
		verbose_name = "Bilder Galerie"
		verbose_name_plural = "Bilder Galerie"



class Aktion(models.Model):
	promo_bild = models.ImageField(upload_to="einstellung/lieferLogo")
	von_datum = models.DateField(null=True, blank=True)
	biss_datum = models.DateField(null=True, blank=True)

	class Meta:
		verbose_name = "Aktion"
		verbose_name_plural = "Aktion"



class LieferungService(models.Model):
	name = models.CharField(max_length=30)
	liefer_logo = models.ImageField(upload_to="einstellung", blank=True, null=True)
	link = models.CharField(max_length=80)