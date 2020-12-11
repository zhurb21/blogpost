from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    compelete = models.BooleanField(default=False)
    created = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title