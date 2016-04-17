from django.db import models


class General(models.Model):
    title = models.CharField(max_length=200)
    under_construction = models.BooleanField(default=False)

    def __str__(self):
        return "General site settings"
