from app.routers.cutting import router as cutting_router
from app.routers.materials import router as materials_router
from app.routers.parts import router as parts_router


__all__ = [
    "cutting_router",
    "materials_router",
    "parts_router",
]