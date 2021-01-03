from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Film(models.Model):
    Title = models.CharField(max_length=250)
    Slug = models.SlugField(unique=True)
    
    Release = models.CharField(max_length=250, blank=True, null=True)

    Genre = models.CharField(max_length=250, blank=True, null=True)

    Description = RichTextField(blank=True, null=True)

    Image = models.CharField(max_length=250, blank=True, null=True)

    URL = models.URLField(max_length=200, blank=True, null=True)

    Views = models.BigIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.Title

    def Snippet(self):
        return self.Title[:30]

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Message = models.TextField()

    def __str__(self):
        return self.Name