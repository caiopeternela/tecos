from django.db import models
from hashlib import md5

# Create your models here.
class Url(models.Model):
    url = models.CharField(unique=True, max_length=512)
    short_url = models.CharField(unique=True, max_length=36)

    def __str__(self):
        return self.url

    @classmethod
    def shorten(self, url):
        temp_url = md5(url.encode()).hexdigest()[:5]
        try: 
            obj = self.objects.create(url=url, short_url=temp_url)
        except:
            obj = self.objects.get(url=url)

        return obj