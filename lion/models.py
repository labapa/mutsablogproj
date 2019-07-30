from django.db import models

# Create your models here.
class Lion(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def _str_(self):
        return self.title

    def summary(self):
        return self.body[:100]