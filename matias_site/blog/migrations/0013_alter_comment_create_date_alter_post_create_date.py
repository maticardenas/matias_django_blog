# Generated by Django 4.1.2 on 2023-10-19 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_alter_comment_create_date_alter_post_create_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 19, 11, 53, 21, 895671, tzinfo=datetime.timezone.utc)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 19, 11, 53, 21, 895437, tzinfo=datetime.timezone.utc)
            ),
        ),
    ]
