# Generated by Django 2.2 on 2020-02-07 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundlookup', '0005_auto_20200206_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='politicalparty',
            name='cap',
            field=models.FloatField(default='5000', verbose_name='Cap'),
        ),
        migrations.AddField(
            model_name='politicalparty',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='Enabled'),
        ),
    ]