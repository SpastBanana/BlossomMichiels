# Generated by Django 3.0.8 on 2021-12-06 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Sitemanager', '0002_delete_shootpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='addImg4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portName', models.CharField(choices=[('creatief', 'creatief'), ('dieren', 'dieren'), ('ethiopië', 'ethiopië'), ('evenementen', 'evenementen'), ('gebouwen', 'gebouwen'), ('kids', 'kids'), ('schilderijen', 'schilderijen'), ('tieners', 'tieners'), ('volwassenen', 'volwassenen'), ('voorstellingen', 'voorstellingen')], max_length=100)),
                ('alignment', models.CharField(choices=[('left', 'left'), ('right', 'right'), ('center', 'center'), ('up', 'up'), ('down', 'down')], max_length=100)),
                ('img1', models.ImageField(upload_to='portfolio-<django.db.models.fields.CharField>/')),
                ('img2', models.ImageField(upload_to='portfolio-<django.db.models.fields.CharField>/')),
                ('img3', models.ImageField(upload_to='portfolio-<django.db.models.fields.CharField>/')),
                ('img4', models.ImageField(upload_to='portfolio-<django.db.models.fields.CharField>/')),
                ('txt', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Add Blocks',
            },
        ),
        migrations.CreateModel(
            name='addImg5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portName', models.CharField(choices=[('creatief', 'creatief'), ('dieren', 'dieren'), ('ethiopië', 'ethiopië'), ('evenementen', 'evenementen'), ('gebouwen', 'gebouwen'), ('kids', 'kids'), ('schilderijen', 'schilderijen'), ('tieners', 'tieners'), ('volwassenen', 'volwassenen'), ('voorstellingen', 'voorstellingen')], max_length=100)),
                ('alignment', models.CharField(choices=[('left', 'left'), ('right', 'right'), ('center', 'center'), ('up', 'up'), ('down', 'down')], max_length=100)),
                ('img1', models.ImageField(upload_to='portfolio-<django.db.models.fields.CharField>/')),
                ('img2', models.ImageField(upload_to='portfolio-<django.db.models.fields.CharField>/')),
                ('img3', models.ImageField(upload_to='portfolio-<django.db.models.fields.CharField>/')),
                ('img4', models.ImageField(upload_to='portfolio-<django.db.models.fields.CharField>/')),
                ('img5', models.ImageField(upload_to='portfolio-<django.db.models.fields.CharField>/')),
                ('txt', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Add Blocks',
            },
        ),
    ]