from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    id_user = models.ForeignKey(User, db_column='id_user', primary_key=True)
    available_credit = models.FloatField(blank=True, null=True)
    gain_obtained = models.FloatField(blank=True, null=True)
    class_customer = models.CharField(max_length=4, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    telephone = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    picture = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_profile'
