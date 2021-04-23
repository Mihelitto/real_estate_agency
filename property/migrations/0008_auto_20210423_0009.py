# Generated by Django 2.2.20 on 2021-04-22 21:09

from django.db import migrations
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException


def parse_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.owners_phonenumber:
            try:
                parsed_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
            except NumberParseException:
                continue
            if phonenumbers.is_valid_number(parsed_phone):
                flat.owner_pure_phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164)
                flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(parse_phonenumbers)
    ]