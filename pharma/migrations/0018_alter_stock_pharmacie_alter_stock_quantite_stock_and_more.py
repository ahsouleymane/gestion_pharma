# Generated by Django 4.1.7 on 2023-06-01 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0017_tourgardecom5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='pharmacie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharma.pharmaciegarde'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantite_stock',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='unite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharma.unite'),
        ),
    ]
