# Generated by Django 2.1.7 on 2019-03-20 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("internet_nl_dashboard", "0004_uploadlog_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="uploadlog",
            old_name="orginal_filename",
            new_name="original_filename",
        ),
    ]
