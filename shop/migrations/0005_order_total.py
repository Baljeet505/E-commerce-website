# Generated by Django 4.2.6 on 2023-10-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_zipcode_order_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]
