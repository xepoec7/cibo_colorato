# Generated by Django 3.2.7 on 2021-11-24 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0006_meistgekaufte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meistgekaufte',
            name='artikel_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artikel_1', to='pos.artikel'),
        ),
        migrations.AlterField(
            model_name='meistgekaufte',
            name='artikel_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artikel_2', to='pos.artikel'),
        ),
        migrations.AlterField(
            model_name='meistgekaufte',
            name='artikel_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artikel_3', to='pos.artikel'),
        ),
        migrations.AlterField(
            model_name='meistgekaufte',
            name='artikel_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artikel_4', to='pos.artikel'),
        ),
    ]
