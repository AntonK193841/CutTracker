import requests

from importer.models import SpecificationPart


class CutTrackerApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def create_part(
        self,
        part: SpecificationPart,
    ) -> dict:
        response = requests.post(
            f"{self.base_url}/api/parts",
            json={
                "drawing_number": part.drawing_number,
                "name": part.name,
                "width": part.width,
                "height": part.height,
                "quantity": part.quantity,
                "material_id": part.material_id,
            },
            timeout=10,
        )

        response.raise_for_status()

        return response.json()