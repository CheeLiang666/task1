# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Stores(models.Model):
    storeid = models.IntegerField(db_column='storeID', primary_key=True)  # Field name made lowercase.
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    storename = models.TextField(db_column='storeName', blank=True, null=True)  # Field name made lowercase.
    storeaddress = models.TextField(db_column='storeAddress', blank=True, null=True)  # Field name made lowercase.
    storephone = models.TextField(db_column='storePhone', default='-')  # Field name made lowercase.
    weekdayopen = models.TextField(db_column='weekDayOpen', blank=True, null=True)  # Field name made lowercase.
    weekdayclose = models.TextField(db_column='weekDayClose', blank=True, null=True)  # Field name made lowercase.
    weekendopen = models.TextField(db_column='weekEndOpen', blank=True, null=True)  # Field name made lowercase.
    weekendclose = models.TextField(db_column='weekEndClose', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.storename

    class Meta:
        managed = True
        db_table = 'stores'
