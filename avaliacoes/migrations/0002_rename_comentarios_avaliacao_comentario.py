# Generated by Django 4.1.3 on 2023-01-18 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("avaliacoes", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="avaliacao", old_name="comentarios", new_name="comentario",
        ),
    ]