from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length = 300)
    bio = models.TextField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length = 160)
    
    def __str__(self):
        return self.name
    
    
class Artwork(models.Model):
    artist = models.ForeignKey(Artist , related_name= 'artwork' ,on_delete=models.CASCADE)
    title = models.CharField(max_length = 400)
    description = models.TextField()
    creation_date = models.DateField()
    image_url = models.URLField()
    
    
    def __str__(self):
        return self.title
    
    
    
class Exhibition(models.Model):
    name = models.CharField(max_length = 300)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location =models.CharField(max_length = 400)
    artworks = models.ManyToManyField(Artist)
    
    
    def __str__(self):
        return self.name