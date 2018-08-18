from django.db import models
from django.contrib.auth.models import User



class EntryType(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Entry(models.Model):

    name = models.CharField(max_length=100, verbose_name='Title of Post')
    type = models.ForeignKey(EntryType, related_name='entries', on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='entry_images/')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
