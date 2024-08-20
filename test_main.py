import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_addition():
    response = client.get("/add/5/3")
    assert response.status_code == 200
    assert response.json() == {"total": 8}


@pytest.mark.parametrize(
    "num1, num2, expected_total",
    [
        (1, 1, 2),
        (10, 20, 30),
        (-5, 5, 0),
        (0, 0, 0),
    ],
)
def test_addition_parametrized(num1, num2, expected_total):
    response = client.get(f"/add/{num1}/{num2}")
    assert response.status_code == 200
    assert response.json() == {"total": expected_total}
