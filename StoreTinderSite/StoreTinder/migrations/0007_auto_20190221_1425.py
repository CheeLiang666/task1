# Generated by Django 2.1.7 on 2019-02-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreTinder', '0006_auto_20190221_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='is_verified',
            field=models.BooleanField(db_column='is_verified'),
        ),
    ]