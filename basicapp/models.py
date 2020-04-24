from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length = 264)
    email = models.EmailField()
    weburl = models.URLField()

    def __str__(self):
        return self.name
