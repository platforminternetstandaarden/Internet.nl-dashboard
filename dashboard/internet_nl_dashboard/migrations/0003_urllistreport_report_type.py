# Generated by Django 3.1.13 on 2021-07-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("internet_nl_dashboard", "0002_auto_20210729_1549"),
    ]

    operations = [
        migrations.AddField(
            model_name="urllistreport",
            name="report_type",
            field=models.CharField(default="web", max_length=10),
        ),
    ]
