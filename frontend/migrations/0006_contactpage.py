# Generated by Django 3.2.9 on 2021-11-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20211111_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(default='Contact info', max_length=25)),
                ('place', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('socials', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Contact Page',
            },
        ),
    ]