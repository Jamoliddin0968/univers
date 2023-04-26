from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from mptt.models import MPTTModel, TreeForeignKey
from pilkit.processors import *


class User(AbstractUser):
    is_full_user = models.BooleanField(default=False)


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(("slug"))
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Sahifa"
        verbose_name_plural = "Sahifalar"

    def link(self):
        return reverse("page_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Category(MPTTModel):
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        help_text="Agar bosh kategoriya bo'lsa majburiy emas",
    )
    title = models.CharField(max_length=50, verbose_name="Nomi")
    page = models.OneToOneField(
        Page,
        verbose_name=("Sahifa"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Sahifa tanlang.Majburiy emas",
    )

    link = models.URLField(
        ("Link"), max_length=200, help_text="Boshqa sayt uchun link.Majburiy emas", null=True, blank=True
    )

    class MPTTMeta:
        order_insertion_by = ["title"]

    def __str__(self) -> str:
        return self.title.title()

    def get_page_link(self):
        if self.link:
            return self.link
        if self.page:
            return self.page.link()
        else:
            return "#"

    class Meta:
        verbose_name = "Menyu"
        verbose_name_plural = "Menyu"


# -------------------------------------------------


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="Muqova rasm", upload_to="images/")
    date = models.DateField(("Vaqti"), auto_now_add=True)
    content = RichTextUploadingField(null=True, blank=True)
    image_bg = ImageSpecField(source="image", processors=[Resize(360, 260)], format="JPEG", options={"quality": 100})

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.title


class Cafedra(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="rasmi", upload_to="cafedra/")
    content = RichTextUploadingField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    image_bg = ImageSpecField(source="image", processors=[Resize(770, 346)], format="JPEG", options={"quality": 100})

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

    image_bg = ImageSpecField(source="image", processors=[Resize(770, 346)], format="JPEG", options={"quality": 100})

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

    image_bg = ImageSpecField(source="image", processors=[Resize(770, 346)], format="JPEG", options={"quality": 100})

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

    image_bg = ImageSpecField(source="image", processors=[Resize(770, 346)], format="JPEG", options={"quality": 100})

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"

    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"pk": self.pk})
