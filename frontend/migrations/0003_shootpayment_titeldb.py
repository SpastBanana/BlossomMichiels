# Generated by Django 3.2.9 on 2021-11-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_shootpayment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='shootpayment',
            name='titelDB',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]