# Generated by Django 3.2.7 on 2021-11-22 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_auto_20211112_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shootpayment',
            name='alinea1Align',
        ),
        migrations.RemoveField(
            model_name='shootpayment',
            name='alinea2Align',
        ),
        migrations.RemoveField(
            model_name='shootpayment',
            name='alinea3Align',
        ),
    ]
