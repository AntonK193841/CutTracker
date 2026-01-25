from app.models.cutting_plan import CuttingPlan


def test_cutting_plan_model():
    plan = CuttingPlan(
        material_id=1,
        used_area=500_000,
        waste_area=500_000,
        utilization=50,
    )

    assert plan.material_id == 1
    assert plan.used_area == 500_000
    assert plan.waste_area == 500_000
    assert plan.utilization == 50