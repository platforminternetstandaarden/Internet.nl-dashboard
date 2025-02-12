# Generated by Django 3.1.13 on 2021-09-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0060_auto_20200908_1055"),
        ("internet_nl_dashboard", "0007_urllist_urls"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urllist",
            name="urls",
            field=models.ManyToManyField(
                related_name="urls_in_dashboard_list_2",
                through="internet_nl_dashboard.TaggedUrlInUrllist",
                to="organizations.Url",
            ),
        ),
    ]
