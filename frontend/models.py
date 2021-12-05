from django.db import models

class shootPayment(models.Model):
    SHOOT_CHOICES = [
        ('Event shoot', 'Event shoot'),
        ('Portret shoot', 'Portret shoot'),
        ('Familie shoot', 'Familie shoot'),
        ('Dieren shoot', 'Dieren shoot'),
        ('Gebouwen shoot', 'Gebouwen shoot'),
    ]

    TEXT_CHOICES = [
        ('left', 'left'),
        ('center', 'center'),
        ('right', 'right'),
    ]

    titel = models.CharField(max_length=25, choices=SHOOT_CHOICES)
    Alinea1 = models.TextField(default="none")
    Alinea2 = models.TextField(default="none")
    Alinea3 = models.TextField(default="none")

    def __str__(self):
        return self.titel

    class Meta:
        verbose_name_plural = "Tarieven"

class contactPage(models.Model):
    titel = models.CharField(max_length=25, default="Contact info")
    place = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    socials = models.CharField(max_length=25)
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.titel

    class Meta:
        verbose_name_plural = "Contact Page"