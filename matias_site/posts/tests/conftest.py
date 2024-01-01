from datetime import datetime

import pytest
from django.contrib.auth.models import User


@pytest.fixture
def post(user: User):
    from blog.models import Post

    Post.objects.create(
        author=user,
        title="Test Post",
        text="Test Text",
        create_date=datetime.strptime("31/12/2022 00:00:00", "%d/%m/%Y %H:%M:%S"),
    )
