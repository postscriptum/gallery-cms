from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    #------------------------------------------
    header = models.BooleanField(default=False)
    footer = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class General(models.Model):
    title = models.CharField(max_length=200)
    under_construction = models.BooleanField(default=False)
    theme = models.ForeignKey(Theme, blank=True, null=True)

    def __str__(self):
        return "General site settings"
