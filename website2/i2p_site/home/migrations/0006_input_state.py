# Generated by Django 4.1.3 on 2022-12-04 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_alter_input_age_alter_input_gender_alter_input_race"),
    ]

    operations = [
        migrations.AddField(
            model_name="input",
            name="state",
            field=models.CharField(default="fill in your info", max_length=50),
        ),
    ]
