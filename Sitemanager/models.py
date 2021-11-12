from django.db import models

class shootPayment(models.Model):
    SHOOT_CHOICES = [
        ('Event shoot', 'Event shoot'),
        ('Portret shoot', 'Portret shoot'),
        ('Familie shoot', 'Familie shoot'),
        ('Dieren shoot', 'Dieren shoot'),
        ('Gebouwen shoot', 'Gebouwen shoot'),
    ]
    titel = models.CharField(max_length=25, choices=SHOOT_CHOICES)
    Alinea1 = models.TextField()
    Alinea2 = models.TextField()
    Alinea3 = models.TextField()

    def __str__(self):
        return self.titel

    class Meta:
        verbose_name_plural = "Tarieven"