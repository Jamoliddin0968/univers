# Generated by Django 4.2 on 2023-04-28 15:30

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("institute", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cafedra",
            old_name="name",
            new_name="title",
        ),
        migrations.RenameField(
            model_name="center",
            old_name="name",
            new_name="title",
        ),
        migrations.RenameField(
            model_name="department",
            old_name="name",
            new_name="title",
        ),
        migrations.RenameField(
            model_name="fakultet",
            old_name="name",
            new_name="title",
        ),
        migrations.AddField(
            model_name="category",
            name="title_en",
            field=models.CharField(max_length=50, null=True, verbose_name="Nomi"),
        ),
        migrations.AddField(
            model_name="category",
            name="title_ru",
            field=models.CharField(max_length=50, null=True, verbose_name="Nomi"),
        ),
        migrations.AddField(
            model_name="category",
            name="title_uz",
            field=models.CharField(max_length=50, null=True, verbose_name="Nomi"),
        ),
        migrations.AlterField(
            model_name="cafedra",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(default=" "),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="cafedra",
            name="image",
            field=models.ImageField(upload_to="images/", verbose_name="Muqova rasm"),
        ),
        migrations.AlterField(
            model_name="center",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(default=" "),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="center",
            name="image",
            field=models.ImageField(upload_to="images/", verbose_name="Muqova rasm"),
        ),
        migrations.AlterField(
            model_name="department",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(default=" "),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="department",
            name="image",
            field=models.ImageField(upload_to="images/", verbose_name="Muqova rasm"),
        ),
        migrations.AlterField(
            model_name="fakultet",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(default=" "),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="fakultet",
            name="image",
            field=models.ImageField(upload_to="images/", verbose_name="Muqova rasm"),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(default=" "),
            preserve_default=False,
        ),
    ]
