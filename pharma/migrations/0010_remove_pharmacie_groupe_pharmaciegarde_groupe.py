# Generated by Django 4.1.7 on 2023-04-26 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0009_alter_pharmaciegarde_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmacie',
            name='groupe',
        ),
        migrations.AddField(
            model_name='pharmaciegarde',
            name='groupe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharma.groupe'),
        ),
    ]
