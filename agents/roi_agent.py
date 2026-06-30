def calculate_roi(industry, employees, revenue):
    """
    Dynamic ROI Calculator
    revenue -> Annual Revenue in Crores
    employees -> Number of Employees
    """

    # -------------------------
    # Implementation Cost
    # -------------------------

    if employees < 100:
        implementation_cost = 20_00_000

    elif employees < 1000:
        implementation_cost = 50_00_000

    elif employees < 5000:
        implementation_cost = 1_00_00_000

    else:
        implementation_cost = 2_00_00_000

    # -------------------------
    # Automation Benefit
    # -------------------------

    automation = {
        "Banking": 0.04,
        "Healthcare": 0.03,
        "Retail": 0.05
    }.get(industry, 0.03)

    # Revenue is entered in Crores
    annual_revenue = revenue * 1_00_00_000

    annual_savings = annual_revenue * automation

    roi = (
        (annual_savings - implementation_cost)
        / implementation_cost
    ) * 100

    payback = (
        implementation_cost / annual_savings
    ) * 12

    return {
        "cost": implementation_cost,
        "savings": annual_savings,
        "roi": round(roi, 2),
        "payback": round(payback, 1)
    }