import os
from datetime import datetime

from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "matias_site.settings")

from pathlib import Path
from typing import TYPE_CHECKING, Callable

import pytest
from openapi_tester import SchemaTester

if TYPE_CHECKING:
    from rest_framework.authtoken.admin import User

CURRENT_PATH = Path().absolute()


@pytest.fixture
def schema_tester_factory() -> Callable:
    def schema_tester(schema_file: Path) -> SchemaTester:
        return SchemaTester(schema_file_path=schema_file)

    return schema_tester


@pytest.fixture
def openapi_client_factory() -> Callable:
    def openapi_client(schema_tester: SchemaTester):
        from openapi_tester.clients import `OpenAPIClient`

        return OpenAPIClient(schema_tester=schema_tester)

    return openapi_client


@pytest.fixture
def user():
    return get_user_model().objects.create_user("test_user")


@pytest.fixture
def post(user: "User"):
    from blog.models import Post

    Post.objects.create(
        author=user,
        title="Test Post",
        text="Test Text",
        create_date=datetime.strptime("31/12/2022 00:00:00", "%d/%m/%Y %H:%M:%S"),
    )
