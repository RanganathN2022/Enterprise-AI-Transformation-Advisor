def discover_ai_opportunities(industry):

    opportunities = {

        "Banking": [
            {
                "use_case": "AI Customer Support Assistant",
                "benefit": "Reduce support cost by 30-40%"
            },
            {
                "use_case": "Loan Approval Automation",
                "benefit": "Faster loan processing"
            },
            {
                "use_case": "Fraud Detection",
                "benefit": "Reduce financial losses"
            }
        ]
    }

    return opportunities.get(
        industry,
        [{
            "use_case": "AI Opportunity Assessment",
            "benefit": "Identify business value"
        }]
    )