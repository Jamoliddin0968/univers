# Generated by Django 4.2 on 2023-04-21 16:22

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0015_alter_category_options_remove_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='content',
        ),
        migrations.RemoveField(
            model_name='category',
            name='date',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=' ', verbose_name='slug'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institute.category')),
            ],
            options={
                'verbose_name': 'Sahifa',
                'verbose_name_plural': 'Sahifalar',
            },
        ),
    ]
