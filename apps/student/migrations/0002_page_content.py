# Generated by Django 4.2 on 2023-04-17 11:43

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=' '),
            preserve_default=False,
        ),
    ]
