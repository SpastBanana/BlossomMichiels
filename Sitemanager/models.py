from django.db import models


class portfolioPages(models.Model):
    portName = models.CharField(max_length=30)
    img1 = models.ImageField(upload_to='portfolio')
    img2 = models.ImageField(upload_to='portfolio')
    img3 = models.ImageField(upload_to='portfolio')

    def __str__(self):
        return self.portName

    class Meta:
        verbose_name_plural = "Portfolio IMG pages"


class innerPortPageItems(models.Model):
    portName = models.CharField(max_length=30)
    rowFormat = models.CharField(max_length=255)
    text = models.TextField(max_length=200)
    portimg1 = models.ImageField(blank=True, null=True, default='none.jpg', upload_to='portfolioFormats')
    portimg2 = models.ImageField(blank=True, null=True, default='none.jpg', upload_to='portfolioFormats')
    portimg3 = models.ImageField(blank=True, null=True, default='none.jpg', upload_to='portfolioFormats')

    def __str__(self):
        return self.portName

    class Meta:
        verbose_name_plural = "Portfolio inner page items"