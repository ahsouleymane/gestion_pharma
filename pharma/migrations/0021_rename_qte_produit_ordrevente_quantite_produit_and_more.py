# Generated by Django 4.1.7 on 2023-06-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0020_ordrevente_date_ajout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordrevente',
            old_name='qte_produit',
            new_name='quantite_produit',
        ),
        migrations.AlterField(
            model_name='ordrevente',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
