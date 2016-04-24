from django.db import models


class Theme(models.Model):
    LAYOUT_CHOICES = (
        ('front/grid_3.html', '3 Column Grid'),
        ('front/grid_4.html', '4 Column Grid'),
        ('front/slides.html', 'Slides'),
        ('front/slides_collapsed.html', 'Collapsed Slides'),
    )
    #------------------------------------------
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    #------------------------------------------
    header = models.BooleanField(default=False)
    jumbotron = models.BooleanField(default=False)
    layout = models.CharField(max_length=50, choices=LAYOUT_CHOICES, default='front/grid_3.html')
    footer = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class General(models.Model):
    title = models.CharField(max_length=200)
    header_text = models.CharField(max_length=200, default='', blank=True)
    jumbotron_content = models.TextField(default='', blank=True)
    footer_text = models.CharField(max_length=200, default='', blank=True)
    under_construction = models.BooleanField(default=False)
    theme = models.ForeignKey(Theme, blank=True, null=True)

    def __str__(self):
        return "General site settings"