# Generated by Django 4.1.3 on 2022-11-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="person", name="name",),
        migrations.AddField(
            model_name="person", name="age", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="person",
            name="gender",
            field=models.CharField(default="prefer not to answer", max_length=50),
        ),
        migrations.AddField(
            model_name="person",
            name="race",
            field=models.CharField(default="prefer not to answer", max_length=50),
        ),
    ]
