from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from PIL import Image
from pilkit.processors import *


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="Muqova rasm", upload_to="images/")
    date = models.DateField(("Vaqti"), auto_now_add=True)
    content = RichTextUploadingField(null=True, blank=True)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Cafedra(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="rasmi", upload_to="cafedra/")
    content = RichTextUploadingField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    image_bg = ImageSpecField(
        source='image',
        processors=[Resize(770, 346)],
        format='JPEG',
        options={'quality': 100}
    )

    class Meta:
        verbose_name = "Kafedra"
        verbose_name_plural = "Kafedralar"

    def get_absolute_url(self):
        return reverse("cafedra_detail", kwargs={"pk": self.pk})


class Fakultet(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="rasmi", upload_to="fakultet/")
    content = RichTextUploadingField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    image_bg = ImageSpecField(
        source='image',
        processors=[Resize(770, 346)],
        format='JPEG',
        options={'quality': 100}
    )

    class Meta:
        verbose_name = "Fakultet"
        verbose_name_plural = "Fakultetlar"

    def get_absolute_url(self):
        return reverse("fakultet_detail", kwargs={"pk": self.pk})


class Center(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="rasmi", upload_to="center/")
    content = RichTextUploadingField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    image_bg = ImageSpecField(
        source='image',
        processors=[Resize(770, 346)],
        format='JPEG',
        options={'quality': 100}
    )
    class Meta:
        verbose_name = "Markaz"
        verbose_name_plural = "Markazlar"
    def get_absolute_url(self):
        return reverse("center_detail", kwargs={"pk": self.pk})


class Department(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="rasmi", upload_to="department/")
    content = RichTextUploadingField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    image_bg = ImageSpecField(
        source='image',
        processors=[Resize(770, 346)],
        format='JPEG',
        options={'quality': 100}
    )
    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"
    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"pk": self.pk})
