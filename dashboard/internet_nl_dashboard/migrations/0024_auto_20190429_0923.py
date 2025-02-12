# Generated by Django 2.2 on 2019-04-29 09:23

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("internet_nl_dashboard", "0023_auto_20190429_0910"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urllist",
            name="scheduled_next_scan",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 4, 28, 9, 23, 16, 512927, tzinfo=datetime.timezone.utc),
                help_text="An indication at what moment the scan will be started. The scan can take a while, thus this does not tell you when a scan will be finished.",
            ),
        ),
    ]
