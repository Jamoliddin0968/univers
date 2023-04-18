# Generated by Django 4.2 on 2023-04-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0006_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafedra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='cafedra/', verbose_name='rasmi')),
                ('content', models.TextField()),
            ],
        ),
    ]
