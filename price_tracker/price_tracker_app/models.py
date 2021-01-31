from django.db import models


# Create your models here.
class Amazon(models.Model):
    class Meta:
        verbose_name_plural = 'amazon'

    URL = models.CharField(max_length=2083)
    Desired_Price = models.FloatField()
    Email = models.EmailField()
    Time = models.DateTimeField(null=True, blank=True)


class Flipkart(models.Model):
    class Meta:
        verbose_name_plural = 'flipkart'

    URL = models.CharField(max_length=2083)
    Desired_Price = models.FloatField()
    Email = models.EmailField()
    Time = models.DateTimeField(null=True, blank=True)


class Snapdeal(models.Model):
    class Meta:
        verbose_name_plural = 'snapdeal'

    URL = models.CharField(max_length=2083)
    Desired_Price = models.FloatField()
    Email = models.EmailField()
    Time = models.DateTimeField(null=True, blank=True)