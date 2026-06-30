def calculate_maturity(industry):

    maturity = {

        "Banking": {

            "Data Readiness": 85,

            "Infrastructure": 75,

            "People & Skills": 70,

            "Leadership": 90,

            "Governance": 80

        },

        "Healthcare": {

            "Data Readiness": 75,

            "Infrastructure": 70,

            "People & Skills": 65,

            "Leadership": 80,

            "Governance": 75

        },

        "Retail": {

            "Data Readiness": 80,

            "Infrastructure": 70,

            "People & Skills": 72,

            "Leadership": 82,

            "Governance": 78

        }

    }

    return maturity.get(industry)