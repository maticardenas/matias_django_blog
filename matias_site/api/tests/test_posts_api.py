from pathlib import Path
from typing import TYPE_CHECKING, Callable

import pytest as pytest
from django.urls import reverse
from freezegun import freeze_time
from openapi_tester import OpenAPIClient, SchemaTester
from rest_framework import status

if TYPE_CHECKING:
    from django.contrib.auth.models import User


CURRENT_PATH = Path(__file__).parent.absolute()

POSTS_API_OAS_PATH = CURRENT_PATH / ".." / "schemas" / "posts_api.yaml"


@pytest.fixture
def post_api_url():
    return reverse("api:post-list")


@pytest.fixture
def schema_tester(schema_tester_factory: Callable):
    return schema_tester_factory(POSTS_API_OAS_PATH)


@pytest.fixture
def client(openapi_client_factory: Callable, schema_tester: SchemaTester) -> OpenAPIClient:
    return openapi_client_factory(schema_tester)


@pytest.mark.django_db
def test_get_posts_with_data(client: OpenAPIClient, user: "User", post_api_url: str, post):
    client.force_authenticate(user=user)
    response = client.get(post_api_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "author": 1,
            "title": "Test Post",
            "text": "Test Text",
            "create_date": "2022-12-31T00:00:00Z",
            "published_date": None,
        }
    ]


@pytest.mark.django_db
def test_get_posts(client: OpenAPIClient, user: "User", post_api_url: str):
    client.force_authenticate(user=user)
    response = client.get(post_api_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


@pytest.mark.django_db
def test_get_posts_unauthorized(client: OpenAPIClient, post_api_url: str):
    response = client.get(post_api_url)

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {"detail": "Authentication credentials were not provided."}
