from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Page(models.Model):
    title = models.CharField(max_length=63)
    content = RichTextUploadingField()
    class Meta:
        verbose_name = ("Sahifa")
        verbose_name_plural = ("Sahifalar")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("skill_page_detail", kwargs={"pk": self.pk})
