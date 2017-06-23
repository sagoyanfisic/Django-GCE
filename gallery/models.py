from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class GalleryUser(models.Model):

    user=models.CharField(max_length=50)
    age=models.IntegerField()
    photo=models.ImageField(upload_to="img")
    slug = models.SlugField(null=False, blank=True)

    def __unicode__(self):
        return self.user

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user)
        super(GalleryUser, self).save(*args, **kwargs)
