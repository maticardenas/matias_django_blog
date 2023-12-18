# Generated by Django 4.1.2 on 2023-12-08 22:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0041_alter_comment_create_date_alter_post_create_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 8, 22, 56, 31, 986076, tzinfo=datetime.timezone.utc)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 8, 22, 56, 31, 985531, tzinfo=datetime.timezone.utc)
            ),
        ),
    ]
