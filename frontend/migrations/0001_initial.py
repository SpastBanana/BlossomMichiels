# Generated by Django 3.2.9 on 2021-11-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shootPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=25)),
                ('context', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
