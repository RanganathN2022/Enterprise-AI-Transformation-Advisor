def generate_summary(
    readiness_score,
    roi,
    risk,
    opportunity_count
):

    if readiness_score >= 80:
        recommendation = "Ready for Enterprise AI Deployment"

    elif readiness_score >= 60:
        recommendation = "Proceed with AI Transformation"

    else:
        recommendation = "Improve AI Readiness Before Deployment"

    if risk == "High":
        priority = "High"

    elif risk == "Medium":
        priority = "Medium"

    else:
        priority = "Low"

    return {

        "recommendation": recommendation,

        "priority": priority,

        "projects": opportunity_count,

        "roi": roi,

        "timeline": "12 Months"

    }