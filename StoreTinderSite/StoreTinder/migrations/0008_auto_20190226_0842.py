# Generated by Django 2.1.7 on 2019-02-26 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreTinder', '0007_auto_20190221_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='id',
            field=models.AutoField(db_column='id', primary_key=True, serialize=False),
        ),
    ]
