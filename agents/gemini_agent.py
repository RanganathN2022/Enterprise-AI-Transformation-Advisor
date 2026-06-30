import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


# =====================================
# AI STRATEGY RECOMMENDATION FUNCTION
# =====================================

def get_ai_recommendations(industry, challenges):

    prompt = f"""
You are a Senior AI Strategy Consultant working for Deloitte.

Your task is to prepare a professional AI Transformation Strategy Report.

Industry:
{industry}

Business Challenges:
{challenges}

Prepare the report using the EXACT structure below.

====================================================================

EXECUTIVE SUMMARY

Write 2-3 professional paragraphs describing the company's current situation,
major business challenges, and how AI can improve business performance.

====================================================================

BUSINESS CHALLENGES

List the identified challenges using bullet points.

====================================================================

RECOMMENDED AI OPPORTUNITIES

Opportunity 1

Objective

Description

Business Benefits

Estimated Business Impact

------------------------------------------------------------

Opportunity 2

Objective

Description

Business Benefits

Estimated Business Impact

------------------------------------------------------------

Opportunity 3

Objective

Description

Business Benefits

Estimated Business Impact

====================================================================

IMPLEMENTATION ROADMAP

Phase 1 (0-3 Months)

Phase 2 (3-6 Months)

Phase 3 (6-12 Months)

====================================================================

RESPONSIBLE AI CONSIDERATIONS

• Data Privacy

• Security

• Fairness

• Explainability

• Governance

====================================================================

EXPECTED BUSINESS OUTCOMES

• Cost Reduction

• Revenue Growth

• Operational Efficiency

• Customer Satisfaction

• Employee Productivity

====================================================================

CONCLUSION

Write a professional executive conclusion.

IMPORTANT INSTRUCTIONS

1. Return ONLY plain text.
2. Do NOT use Markdown.
3. Do NOT use ** symbols.
4. Do NOT use # headings.
5. Use proper paragraphs.
6. Leave one blank line between sections.
7. Make the report professional like Deloitte, EY, Accenture or PwC.
8. Keep the report around 700-1000 words.
"""

    response = model.generate_content(prompt)

    return response.text