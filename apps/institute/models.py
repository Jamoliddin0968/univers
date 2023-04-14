from django.db import models
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="Muqova rasm",upload_to="images/")
    date = models.DateField(("Vaqti"), auto_now_add=True)
    content = RichTextUploadingField(null=True,blank=True)
    