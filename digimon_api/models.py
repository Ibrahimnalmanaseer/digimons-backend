from django.db import models


class Digimon(models.Model):

    email=models.EmailField(default='test@test.com')
    name=models.CharField(max_length=255)
    img=models.URLField()
    level=models.TextField()

