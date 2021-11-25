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

class portfolioRenders(models.Model):
    TYPE_CHOICES = (
        ('format-1', 'format-1'),
        ('format-2', 'format-2'),
        ('format-3', 'format-3'),
        ('format-4', 'format-4'),
    )
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)

    if type == 'format-1' or type == 'format-2':
        print("ass")

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Portfolio"