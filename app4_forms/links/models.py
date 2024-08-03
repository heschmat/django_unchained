from django.db import models

from django.utils.text import slugify

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length= 25, unique= True)
    url = models.URLField(max_length= 100)
    # If not slug provided, then it'll be created:
    # my awesome link => my-awesome-link
    slug = models.SlugField(max_length= 25, unique= True, blank= True)
    n_clicks = models.PositiveIntegerField(default= 0)

    def __str__(self) -> str:
        return f'{self.slug} | {self.n_clicks}'
    
    def update_clicks(self):
        self.n_clicks += 1
        self.save() # only so it'll update the record in the database

    # Override the `save()` method to cover/generate when no `slug` is provided.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
