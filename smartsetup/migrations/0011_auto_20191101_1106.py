# Generated by Django 2.2.6 on 2019-11-01 10:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('smartsetup', '0010_auto_20191029_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartNoteItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_code', models.CharField(max_length=256)),
                ('item_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='GJournalMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Date/Time')),
                ('ref_number', models.PositiveIntegerField(default=100)),
                ('description', models.CharField(default='', max_length=256)),
                ('total_debit', models.FloatField(default=0)),
                ('total_credit', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='expensemain',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Expense Date/Time'),
        ),
        migrations.AlterField(
            model_name='expensemain',
            name='payee',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Payee'),
        ),
        migrations.CreateModel(
            name='GJournalDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=256)),
                ('debit', models.FloatField(default=0)),
                ('credit', models.FloatField(default=0)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smartsetup.ChartSubCategory')),
                ('journal_main_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='smartsetup.GJournalMain')),
            ],
        ),
    ]