# Generated by Django 2.2.5 on 2019-10-08 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartsetup', '0006_receiptdetails_receiptmain'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiptdetails',
            name='receipt_main_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='smartsetup.ReceiptMain'),
        ),
    ]
