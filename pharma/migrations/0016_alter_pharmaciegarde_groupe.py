# Generated by Django 4.1.7 on 2023-05-12 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0015_alter_tourgarde_debut_tour_alter_tourgarde_fin_tour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmaciegarde',
            name='groupe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharma.groupe'),
        ),
    ]
