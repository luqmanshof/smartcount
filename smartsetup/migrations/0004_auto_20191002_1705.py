# Generated by Django 2.2.5 on 2019-10-02 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartsetup', '0003_auto_20190926_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setupinventoryitems',
            name='inventory_category_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartsetup.SetupInventoryCategory', verbose_name='Inventory Category'),
        ),
    ]
