from pathlib import Path
from typing import Callable

import pytest as pytest
from openapi_tester import OpenAPIClient, SchemaTester

CURRENT_PATH = Path(__file__).parent.absolute()


@pytest.fixture
def schema_tester(schema_tester_factory: Callable):
    return schema_tester_factory(CURRENT_PATH / ".." / "schemas" / "posts_api.yaml")


@pytest.fixture
def client(openapi_client_factory: Callable, schema_tester: SchemaTester) -> OpenAPIClient:
    return openapi_client_factory(schema_tester)


@pytest.mark.django_db
def test_get_posts(client: OpenAPIClient):
    response = client.get("/api/post/")

    assert response.status_code == 200
    assert response.json() == []
