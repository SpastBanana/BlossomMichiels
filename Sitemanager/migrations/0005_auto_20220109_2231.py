# Generated by Django 3.2.7 on 2022-01-09 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sitemanager', '0004_auto_20220109_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innerportpageitems',
            name='portimg1',
            field=models.ImageField(blank=True, default='none.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='innerportpageitems',
            name='portimg2',
            field=models.ImageField(blank=True, default='none.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='innerportpageitems',
            name='portimg3',
            field=models.ImageField(blank=True, default='none.jpg', null=True, upload_to=''),
        ),
    ]
