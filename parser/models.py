from django.db import models

class PhoneParser(models.Model):
    title = models.CharField(max_length=100)
    title_text = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='')
    cost = models.CharField(max_length=100)

    def __str__(self):
        return self.title

