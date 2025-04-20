from django.db import models

class PageContent(models.Model):
    title     = models.CharField("Title", max_length=200)
    heading   = models.CharField("H1", max_length=200)
    paragraph = models.TextField("Párrafo")
    image     = models.ImageField("Imagen", upload_to='images/')

    def __str__(self):
        return "Home Content"
