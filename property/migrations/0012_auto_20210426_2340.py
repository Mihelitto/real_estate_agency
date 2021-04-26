# Generated by Django 2.2.20 on 2021-04-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20210424_1637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={'verbose_name': 'Жалоба', 'verbose_name_plural': 'Жалобы'},
        ),
        migrations.AlterModelOptions(
            name='flat',
            options={'verbose_name': 'Квартира', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AlterModelOptions(
            name='owner',
            options={'verbose_name': 'Собственник', 'verbose_name_plural': 'Собственники'},
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(db_index=True, verbose_name='Новостройка'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(db_index=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
