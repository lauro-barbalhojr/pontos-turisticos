# Generated by Django 4.1.3 on 2022-11-23 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("atracoes", "0001_initial"),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pontoturistico",
            name="atracoes",
            field=models.ManyToManyField(to="atracoes.atracao"),
        ),
    ]
