# Generated by Django 4.1.7 on 2023-05-16 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0016_alter_pharmaciegarde_groupe'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourGardeCom5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut_tour', models.DateField(null=True)),
                ('fin_tour', models.DateField(null=True)),
                ('groupe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharma.groupe')),
            ],
        ),
    ]
