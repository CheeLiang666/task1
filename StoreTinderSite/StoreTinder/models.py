from django.db import models
# Create your models here.
class Stores(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    name = models.TextField(db_column='name')
    latitude = models.FloatField(db_column='latitude')
    longitude = models.FloatField(db_column='longitude')
    address = models.FloatField(db_column='address')
    source = models.TextField(db_column='source')
    metadata = models.TextField(db_column='metadata')
    created_at = models.DateTimeField(db_column='created_at')
    updated_at = models.DateTimeField(db_column='updated_at')
    is_verified = models.BooleanField(db_column='is_verified')

    def __str__(self):
        return self.name