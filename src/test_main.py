from fastapi.testclient import TestClient
from scraper import scraper
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == scraper()  # test the format of the scraped data


