# Generated by Django 4.1 on 2022-10-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppCoder", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Familiar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=40)),
                ("apellido", models.CharField(max_length=40)),
                ("edad", models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name="Curso",
        ),
        migrations.DeleteModel(
            name="Entregables",
        ),
        migrations.DeleteModel(
            name="Estudiante",
        ),
        migrations.DeleteModel(
            name="Profesor",
        ),
    ]