# Generated by Django 4.1.7 on 2023-03-16 11:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pharma', '0003_paysville_unite_remove_pharmacieandaccount_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PharmacieAndAccount',
            new_name='Pharmacie',
        ),
    ]
