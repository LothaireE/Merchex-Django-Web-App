# Generated by Django 4.1.3 on 2022-11-17 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_offer_band'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='type',
            new_name='offer_type',
        ),
    ]
