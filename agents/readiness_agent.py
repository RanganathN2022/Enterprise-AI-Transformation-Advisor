def calculate_readiness(employees, revenue):

    score = 0

    if employees >= 5000:
        score += 25
    elif employees >= 1000:
        score += 20
    else:
        score += 10

    revenue = str(revenue)

    if "1000" in revenue:
        score += 25
    elif "500" in revenue:
        score += 20
    else:
        score += 10

    score += 20
    score += 20

    return score