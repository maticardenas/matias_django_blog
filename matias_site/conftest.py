import os

import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "matias_site.settings")
django.setup()

from pathlib import Path
from typing import Callable

import pytest
from openapi_tester import SchemaTester

CURRENT_PATH = Path().absolute()


@pytest.fixture
def schema_tester_factory() -> Callable:
    def schema_tester(schema_file: Path) -> SchemaTester:
        return SchemaTester(schema_file_path=str(schema_file))

    return schema_tester


@pytest.fixture
def openapi_client_factory() -> Callable:
    def openapi_client(schema_tester: SchemaTester):
        from openapi_tester.clients import OpenAPIClient

        return OpenAPIClient(schema_tester=schema_tester)

    return openapi_client


@pytest.fixture
def user():
    return get_user_model().objects.create_user("test_user")
