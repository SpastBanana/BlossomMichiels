# Generated by Django 3.2.7 on 2022-01-09 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sitemanager', '0002_innerportpageitems_portimg4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='innerportpageitems',
            name='portimg4',
        ),
    ]
