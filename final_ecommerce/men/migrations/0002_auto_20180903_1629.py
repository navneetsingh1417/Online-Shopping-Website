# Generated by Django 2.0.2 on 2018-09-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='men',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]