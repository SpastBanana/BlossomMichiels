from django.db import models

class shootPayment(models.Model):
    titelDB = models.CharField(max_length=25)
    titel = models.CharField(max_length=25)
    context = models.TextField()

    def __str__(self):
        return self.titelDB

    class Meta:
        verbose_name_plural = "shootPayment"