from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_cutting_calculation():
    response = client.post(
        "/api/cutting/calculate",
        json={
            "sheet_width": 1000,
            "sheet_height": 1000,
            "parts": [
                {
                    "name": "Part A",
                    "width": 500,
                    "height": 500,
                    "quantity": 2,
                }
            ],
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["sheet_area"] == 1_000_000
    assert data["placed_area"] == 500_000
    assert data["waste_area"] == 500_000
    assert data["utilization"] == 50

    assert len(data["placements"]) == 2
    assert len(data["unplaced_parts"]) == 0


def test_cutting_rejects_invalid_sheet():
    response = client.post(
        "/api/cutting/calculate",
        json={
            "sheet_width": 0,
            "sheet_height": 1000,
            "parts": [
                {
                    "name": "Part A",
                    "width": 100,
                    "height": 100,
                    "quantity": 1,
                }
            ],
        },
    )

    assert response.status_code == 422


def test_cutting_reports_unplaced_parts():
    response = client.post(
        "/api/cutting/calculate",
        json={
            "sheet_width": 100,
            "sheet_height": 100,
            "parts": [
                {
                    "name": "Large Part",
                    "width": 500,
                    "height": 500,
                    "quantity": 1,
                }
            ],
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data["placements"]) == 0
    assert len(data["unplaced_parts"]) == 1