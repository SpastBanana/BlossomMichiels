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


class addImg4(models.Model):
    
    presetChoises = [
        ('pre-1', 'pre-1'),
        ('pre-2', 'pre-2'),
        ('pre-3', 'pre-3'),
        ('pre-4', 'pre-4'),
    ]

    def uploadFolder(instance, filename):
        return "portfolio/" + str(instance.title) + "/" + str(filename)

    preset = models.CharField(choices=presetChoises, max_length=100)
    title = models.CharField(max_length=50)
    img1 = models.ImageField(upload_to=uploadFolder)
    img2 = models.ImageField(upload_to=uploadFolder)
    img3 = models.ImageField(upload_to=uploadFolder)
    img4 = models.ImageField(upload_to=uploadFolder)
    txt = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Format 4 foto's"


class addImg5(models.Model):

    presetChoises = [
        ('pre-1', 'pre-1'),
        ('pre-2', 'pre-2'),
        ('pre-3', 'pre-3'),
        ('pre-4', 'pre-4'),
    ]

    def uploadFolder(instance, filename):
        return "portfolio/" + str(instance.title) + "/" + str(filename)

    
    title = models.CharField(max_length=50)
    preset = models.CharField(choices=presetChoises, max_length=100)
    img1 = models.ImageField(upload_to=uploadFolder)
    img2 = models.ImageField(upload_to=uploadFolder)
    img3 = models.ImageField(upload_to=uploadFolder)
    img4 = models.ImageField(upload_to=uploadFolder)
    img5 = models.ImageField(upload_to=uploadFolder)
    txt = models.TextField()

    def __str__(self):
        return self.portName

    class Meta:
        verbose_name_plural = "Format 5 foto's"
