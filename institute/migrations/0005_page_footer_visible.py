# Generated by Django 4.2 on 2023-04-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("institute", "0004_remove_category_w_cafedra_content_en_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="footer_visible",
            field=models.BooleanField(
                default=False,
                help_text="Footer pageda ko'rinishi",
                verbose_name="Sayt haritasida korinishi",
            ),
        ),
    ]
