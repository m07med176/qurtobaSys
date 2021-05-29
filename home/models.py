from django.db import models

class Test(models.Model):
    test = models.CharField(max_length=200)

    def __str__(self):
        return str(self.test)
