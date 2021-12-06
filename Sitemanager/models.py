from django.db import models
from frontend.views import portPageView


class addImg4(models.Model):
    PAGE_CHOICES = [
        ('creatief', 'creatief'),
        ('dieren', 'dieren'),
        ('ethiopië', 'ethiopië'),
        ('evenementen', 'evenementen'),
        ('gebouwen', 'gebouwen'),
        ('kids', 'kids'),
        ('schilderijen', 'schilderijen'),
        ('tieners', 'tieners'),
        ('volwassenen', 'volwassenen'),
        ('voorstellingen', 'voorstellingen'),
    ]

    TEXT_ALIGNMENT_CHOICES = [
        ('left', 'left'),
        ('right', 'right'),
        ('center', 'center'),
        ('up', 'up'),
        ('down', 'down'),
    ]

    # portName = models.TextField(choices=PAGE_CHOICES , max_length=100)
    portName = PAGE_CHOICES
    # alignment = models.CharField(choices=TEXT_ALIGNMENT_CHOICES, max_length=100)
    alignment = TEXT_ALIGNMENT_CHOICES
    img1 = models.ImageField(upload_to = 'portfolio-' + str(portName) + '/')
    img2 = models.ImageField(upload_to = 'portfolio-' + str(portName) + '/')
    img3 = models.ImageField(upload_to = 'portfolio-' + str(portName) + '/')
    img4 = models.ImageField(upload_to = 'portfolio-' + str(portName) + '/')
    txt = models.TextField()

    def __str__(self):
        return self.portName

    class Meta:
        verbose_name_plural = "Format 4 foto's"




class addImg5(models.Model):
    PAGE_CHOICES = [
        ('creatief', 'creatief'),
        ('dieren', 'dieren'),
        ('ethiopië', 'ethiopië'),
        ('evenementen', 'evenementen'),
        ('gebouwen', 'gebouwen'),
        ('kids', 'kids'),
        ('schilderijen', 'schilderijen'),
        ('tieners', 'tieners'),
        ('volwassenen', 'volwassenen'),
        ('voorstellingen', 'voorstellingen'),
    ]

    TEXT_ALIGNMENT_CHOICES = [
        ('left', 'left'),
        ('right', 'right'),
        ('center', 'center'),
        ('up', 'up'),
        ('down', 'down'),
    ]

    portName = models.CharField(choices=PAGE_CHOICES, max_length=100)
    alignment = models.CharField(choices=TEXT_ALIGNMENT_CHOICES, max_length=100)
    img1 = models.ImageField(upload_to='portfolio-' + portName + '/')
    img2 = models.ImageField(upload_to='portfolio-' + portName + '/')
    img3 = models.ImageField(upload_to='portfolio-' + portName + '/')
    img4 = models.ImageField(upload_to='portfolio-' + portName + '/')
    img5 = models.ImageField(upload_to='portfolio-' + portName + '/')
    txt = models.TextField()

    def __str__(self):
        return self.portName

    class Meta:
        verbose_name_plural = "Format 6 foto's"
