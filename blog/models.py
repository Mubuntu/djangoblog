from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField
    created_date = models.DateField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

        # tostring methode
        def __str__(self):
            return self.title


''' na declaratie moet je de models aanmaken in de module door in de cli 
    python manage.py makemigrations blog uit te voeren hier zal je in de blog applicatie de model voor de tabel Post aanmaken
    
    na het aanmaken van de migration file moet je ook appliceren op de database doe dit door in de cli:
    python manage.py migrate blog uit te voeren
    '''
