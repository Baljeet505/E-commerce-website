# Generated by Django 4.2.6 on 2023-10-23 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='zipcode',
            new_name='zip',
        ),
    ]
