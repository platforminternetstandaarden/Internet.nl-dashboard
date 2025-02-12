# Generated by Django 3.1.1 on 2020-10-06 13:09

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("internet_nl_dashboard", "0042_auto_20200530_1735"),
    ]

    operations = [
        migrations.AddField(
            model_name="dashboarduser",
            name="mail_preferred_language",
            field=django_countries.fields.CountryField(default="EN", max_length=2),
        ),
        migrations.AddField(
            model_name="dashboarduser",
            name="mail_preferred_mail_address",
            field=models.EmailField(
                blank=True,
                help_text="This address can deviate from the account mail address for password resets and other account features.",
                max_length=254,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="dashboarduser",
            name="mail_send_mail_after_scan_finished",
            field=models.BooleanField(
                default=False,
                help_text="After a scan is finished, an e-mail is sent informing the user that a report is ready.",
            ),
        ),
    ]
