from django.db import models
from django.urls import reverse
# Create your models here.
class Stores(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(db_column='name')
    latitude = models.FloatField(db_column='latitude')
    longitude = models.FloatField(db_column='longitude')
    address = models.TextField(db_column='address')
    source = models.TextField(db_column='source')
    metadata = models.TextField(db_column='metadata')
    created_at = models.DateTimeField(db_column='created_at')
    updated_at = models.DateTimeField(db_column='updated_at')
    is_verified = models.BooleanField(db_column='is_verified')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('StoreTinder:detail', args=[str(self.id)])