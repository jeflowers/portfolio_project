from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/') # create
    summary = models.CharField(max_length=200) #

    # Display summary of work on the screen.
    def __str__(self):
        return self.summary