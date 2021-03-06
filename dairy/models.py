from django.db import models

# Create your models here.
class done(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title+" "+str(self.date.date())

    class Meta:
        ordering = ['date']
