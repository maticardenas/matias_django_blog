# Generated by Django 4.1.2 on 2023-10-29 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0030_alter_comment_create_date_alter_post_create_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 29, 14, 10, 47, 415725, tzinfo=datetime.timezone.utc)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 29, 14, 10, 47, 415439, tzinfo=datetime.timezone.utc)
            ),
        ),
    ]
