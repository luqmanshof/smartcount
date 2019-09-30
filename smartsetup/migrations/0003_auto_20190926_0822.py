# Generated by Django 2.2.5 on 2019-09-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartsetup', '0002_setupclients_setupinventorycategory_setupinventoryitems_setupvendors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setupinventorycategory',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setupinventorycategory',
            name='inventory_category_code',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='setupinventoryitems',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setupinventoryitems',
            name='inventory_code',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]
