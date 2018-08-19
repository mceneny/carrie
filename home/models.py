from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError



class EntryType(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Entry(models.Model):

    name = models.CharField(max_length=100, verbose_name='Title of Post')
    type = models.ForeignKey(EntryType, related_name='entries', on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/entries')
    image_description = models.CharField(max_length=150, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - (' + self.type.name + ')'

    def clean(self):
        super().clean()

        if self.image:
            if not self.image_description:
                raise ValidationError('A description is required with an image.')
