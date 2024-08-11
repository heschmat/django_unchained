from django.db import models

# Create your models here.
class Profile(models.Model):
    BG_SELEKTION = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow')
    )
    name = models.CharField(max_length= 20)
    slug = models.SlugField(max_length= 20)
    bg_color = models.CharField(max_length= 10, choices= BG_SELEKTION)

    def __str__(self):
        return self.name

class Link(models.Model):
    text = models.CharField(max_length= 100)
    url = models.URLField(max_length= 150)
    
    profile = models.ForeignKey(
        Profile,
        # If a profile is deleted, delete the links associated with it as well.
        on_delete= models.CASCADE,
        # This way, a `profile` can access its `links` via: `profile.links`
        related_name= 'links'
    )

    def __str__(self):
        return f'{self.profile.name} => {self.text}'