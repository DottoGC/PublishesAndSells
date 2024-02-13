from django.db import models

# Create your models here.
class Web(models.Model):
    id = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    mision = models.CharField(max_length=1000, blank=True, null=True)
    vision = models.CharField(max_length=1000, blank=True, null=True)
    eslogan = models.CharField(max_length=200, blank=True, null=True)
    aboutme = models.CharField(max_length=1000, blank=True, null=True)
    logo = models.CharField(max_length=200, blank=True, null=True)
    video = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web'

    def __str__(self):
        return self.nombre

