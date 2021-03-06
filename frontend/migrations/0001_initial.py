# Generated by Django 3.2.7 on 2021-11-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aktion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_bild', models.ImageField(upload_to='einstellung/lieferLogo')),
                ('von_datum', models.DateField(blank=True, null=True)),
                ('biss_datum', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Aktion',
                'verbose_name_plural': 'Aktion',
            },
        ),
        migrations.CreateModel(
            name='BilderGalerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bild', models.ImageField(upload_to='einstellung/gallery')),
            ],
            options={
                'verbose_name': 'Bilder Galerie',
                'verbose_name_plural': 'Bilder Galerie',
            },
        ),
        migrations.CreateModel(
            name='Einstellung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('tel', models.CharField(blank=True, max_length=12, null=True)),
                ('instagram', models.CharField(blank=True, max_length=80, null=True)),
                ('facebook', models.CharField(blank=True, max_length=80, null=True)),
                ('home_page_cover_bild', models.ImageField(blank=True, null=True, upload_to='einstellung/cover')),
                ('uber_uns_text', models.TextField()),
                ('uber_uns_bild', models.ImageField(blank=True, null=True, upload_to='einstellung/cover')),
                ('offnungs_zeit_von', models.TimeField(blank=True, null=True)),
                ('offnungs_zeit_bis', models.TimeField(blank=True, null=True)),
                ('freier_tag', models.CharField(blank=True, choices=[('Mon', 'Montag'), ('Die', 'Dienstag'), ('Mit', 'Mittwoch'), ('Don', 'Donnerstag'), ('Fre', 'Freitag'), ('Sam', 'Samstag'), ('Son', 'Sonntag')], default='Mon', max_length=3)),
            ],
            options={
                'verbose_name': 'Einstellung',
                'verbose_name_plural': 'Einstellung',
            },
        ),
        migrations.CreateModel(
            name='LieferungService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('liefer_logo', models.ImageField(blank=True, null=True, upload_to='einstellung')),
                ('link', models.CharField(max_length=80)),
            ],
        ),
    ]
