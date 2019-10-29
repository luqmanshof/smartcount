# Generated by Django 2.2.6 on 2019-10-08 16:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('smartsetup', '0008_auto_20191008_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiptmain',
            name='receipt_date',
        ),
        migrations.AddField(
            model_name='receiptmain',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]