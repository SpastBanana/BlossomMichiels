from django.db import models

class homeIMG(models.Model):
    titel = models.CharField(max_length=25, default="Contact info")
    place = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    socials = models.CharField(max_length=25)
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.titel

    class Meta:
        verbose_name_plural = "IMG-Home"

class homeText(models.Model):
    titel = models.CharField(max_length=25, default="Contact info")
    place = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    socials = models.CharField(max_length=25)
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.titel

    class Meta:
        verbose_name_plural = "Text-Home"