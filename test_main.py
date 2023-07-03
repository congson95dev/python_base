"""
This module provides tests for the endpoints of the Wikipedia API.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_main():
    """
    Test the root endpoint to ensure that the server is running and returns the correct message.
    """

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}
