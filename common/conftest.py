import pytest
from model_bakery import baker


@pytest.fixture
def new_blog():
    return baker.make("common.Blog")
