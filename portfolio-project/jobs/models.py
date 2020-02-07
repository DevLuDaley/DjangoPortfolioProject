from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
   # url = models.CharField(max_length=200, blank=True)


# def image_tag(self):
#    return u'<img src="%s" />' %
# self.image.url
