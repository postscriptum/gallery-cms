from django.db import models
from colorful.fields import RGBColorField
from ckeditor_uploader.fields import RichTextUploadingField


class Theme(models.Model):
    LAYOUT_CHOICES = (
        ('front/grid_3.html', '3-Column Grid'),
        ('front/grid_4.html', '4-Column Grid'),
        ('front/grid_6.html', '6-Column Grid'),
        ('front/slides.html', 'Slides'),
    )
    #------------------------------------------
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    #------------------------------------------
    header = models.BooleanField("Show header menu", default=False)
    jumbotron = models.BooleanField("Show info block", default=False)
    layout = models.CharField(max_length=50, choices=LAYOUT_CHOICES, default='front/grid_3.html')
    footer = models.BooleanField("Show footer", default=False)
    #------------------------------------------
    bg_color = RGBColorField("Primary background color", default='#FFFFFF')
    text_color = RGBColorField("Primary text color", default='#000000')
    panel_bg_color = RGBColorField("Secondary background color", default='#C0C0C0')
    panel_text_color = RGBColorField("Secondary text color", default='#000000')

    def __str__(self):
        return self.name


class General(models.Model):
    title = models.CharField("Site title text", max_length=200)
    theme = models.ForeignKey(Theme, blank=True, null=True, verbose_name="Theme")
    header_text = models.CharField("Home link text", max_length=200, default='', blank=True)
    jumbotron_content = RichTextUploadingField("Info block content", default='', blank=True)
    footer_text = RichTextUploadingField("Footer content", default='', blank=True)
    under_construction = models.BooleanField(default=False)

    def __str__(self):
        return "General site settings"

    class Meta:
        verbose_name_plural = "General"
