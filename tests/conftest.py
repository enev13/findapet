from typing import Generator

import pytest
from fastapi.testclient import TestClient

# from app.core.config import settings
from app.db.database import SessionLocal
from app.main import app

# from sqlalchemy.orm import Session


# from app.tests.utils.user import authentication_token_from_email
# from app.tests.utils.utils import get_superuser_token_headers


@pytest.fixture(scope="session")
def db() -> Generator:
    """Yield a new database session for each test"""
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    """Yield a new test client for each test"""
    with TestClient(app) as c:
        yield c


# @pytest.fixture(scope="module")
# def superuser_token_headers(client: TestClient) -> Dict[str, str]:
#     return get_superuser_token_headers(client)


# @pytest.fixture(scope="module")
# def normal_user_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
#     return authentication_token_from_email(
#         client=client, email=settings.EMAIL_TEST_USER, db=db
#    )
