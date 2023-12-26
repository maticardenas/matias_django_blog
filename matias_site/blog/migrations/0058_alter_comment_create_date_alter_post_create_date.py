# Generated by Django 4.1.2 on 2023-12-18 21:54

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0057_alter_comment_create_date_alter_post_create_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 18, 21, 54, 33, 584570, tzinfo=datetime.timezone.utc)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 18, 21, 54, 33, 584229, tzinfo=datetime.timezone.utc)
            ),
        ),
    ]
