# Generated by Django 2.1 on 2018-08-19 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image_description',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
