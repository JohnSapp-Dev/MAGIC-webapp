# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WaitTimes(models.Model):
    attraction_id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    theme_park = models.TextField(db_column='Theme Park', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    land = models.TextField(db_column='Land', blank=True, null=True)  # Field name made lowercase.
    attraction = models.TextField(db_column='Attraction', blank=True, null=True)  # Field name made lowercase.
    is_open = models.IntegerField(db_column='Is Open', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wait_time = models.BigIntegerField(db_column='Wait Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wait_times'

    def __str__(self):
        return f"Id: {self.attraction_id}\nTheme Park: {self.theme_park}\nLand: {self.land}\nAttration: {self.attraction}\nIs Open: {self.is_open}\nWait Time: {self.wait_time}\nUpdated {self.updated}"
