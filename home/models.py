from django.db import models


# Create your models here.
class Qrcode(models.Model):
    TYPE = (
        ('png', 'png'),
        ('svg', 'svg'),
    )
    text = models.TextField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE)

    def __str__(self):
        return self.text
