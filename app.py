import streamlit as st

from agents.opportunity_agent import discover_ai_opportunities
from agents.readiness_agent import calculate_readiness
from agents.roi_agent import calculate_roi
from agents.risk_agent import assess_risk
from agents.roadmap_agent import generate_roadmap
from agents.gemini_agent import get_ai_recommendations
from agents.summary_agent import generate_summary
from agents.maturity_agent import calculate_maturity
from utils.chart_generator import maturity_chart
from reports.pdf_generator import generate_pdf

st.set_page_config(
    page_title="Enterprise AI Transformation Advisor",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2103/2103633.png",
        width=80
    )

    st.title("Enterprise AI")

    st.markdown("---")

    st.markdown("### Navigation")

    st.write("🏠 Dashboard")

    st.write("📊 AI Maturity")

    st.write("💰 ROI Analysis")

    st.write("🛡 Responsible AI")

    st.write("🗺 Roadmap")

    st.write("📄 PDF Report")

    st.markdown("---")

    st.success("Version 2.0")

st.title("🤖 Enterprise AI Transformation Advisor")

st.caption(
    "AI Consulting Platform for Enterprise Readiness, ROI Assessment, Responsible AI and Digital Transformation."
)

st.divider()

company_name = st.text_input("Company Name")

industry = st.selectbox(
    "Industry",
    ["Banking", "Healthcare", "Retail"]
)

employee_count = st.number_input(
    "Employees",
    min_value=1,
    step=1
)

annual_revenue = st.number_input(
    "Annual Revenue (Crores ₹)",
    min_value=1,
    step=1
)

business_challenges = st.text_area(
    "Business Challenges",
    height=120
)

submit = st.button("🚀 Assess Company")

if submit:

    opportunities = discover_ai_opportunities(industry)

    readiness_score = calculate_readiness(
        employee_count,
        annual_revenue
    )

    roi_result = calculate_roi(
    industry,
    employee_count,
    annual_revenue
)

    risk_result = assess_risk(industry)

    roadmap = generate_roadmap(industry)

    maturity = calculate_maturity(industry)

    summary = generate_summary(
        readiness_score,
        roi_result["roi"],
        risk_result["risk"],
        len(opportunities)
    )

    ai_report = get_ai_recommendations(
        industry,
        business_challenges
    )

    st.success("Assessment Completed Successfully")

    st.subheader("🏢 Company Profile")

    c1, c2 = st.columns(2)

    with c1:
        st.write("**Company:**", company_name)
        st.write("**Industry:**", industry)

    with c2:
        st.write("**Employees:**", employee_count)
        st.write("**Revenue:**", f"₹{annual_revenue} Crores")

    st.divider()

    st.subheader("📋 Executive Summary")

    c1, c2 = st.columns(2)

    with c1:
        st.info(summary["recommendation"])
        st.metric("Priority", summary["priority"])

    with c2:
        st.metric("Recommended Projects", summary["projects"])
        st.metric("Timeline", summary["timeline"])

    st.divider()

    st.subheader("📈 Executive Dashboard")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("AI Readiness", f"{readiness_score}/100")

    with c2:
        st.metric("ROI", f"{roi_result['roi']}%")

    with c3:
        st.metric("Risk", risk_result["risk"])

    st.divider()

    st.subheader("📊 AI Maturity Assessment")

    chart = maturity_chart(maturity)
    st.pyplot(chart)

    st.divider()

    st.subheader("📊 AI Readiness")

    st.metric("Readiness Score", f"{readiness_score}/100")
    st.progress(readiness_score)

    # =====================================
# ROI ANALYSIS
# =====================================

    st.divider()

    st.subheader("💰 ROI Analysis")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Implementation Cost",
            f"INR {roi_result['cost']:,}"
        )

    with col2:
        st.metric(
            "Annual Savings",
            f"INR {roi_result['savings']:,}"
        )

    with col3:
        st.metric(
            "ROI",
            f"{roi_result['roi']}%"
        )

    with col4:
        st.metric(
            "Payback Period",
            f"{roi_result['payback']} Months"
        )
        
    st.divider()

    st.subheader("🛡 Responsible AI Assessment")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Risk", risk_result["risk"])

    with c2:
        st.metric("Privacy", risk_result["privacy"])

    with c3:
        st.metric("Explainability", risk_result["explainability"])

    st.divider()

    st.subheader("🗺 AI Transformation Roadmap")

    for step in roadmap:
        st.write(f"✅ {step}")

   
# ======================
# PDF REPORT
# ======================
    st.divider()
    st.subheader("📄 Generate AI Assessment Report")

    pdf_file = generate_pdf(
        company_name=company_name,
        industry=industry,
        employees=employee_count,
        revenue=annual_revenue,
        readiness=readiness_score,
        maturity=maturity,
        roi_result=roi_result,
        risk_result=risk_result,
        roadmap=roadmap,
        ai_report=ai_report
    )

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="📥 Download AI Transformation Report",
            data=file,
            file_name="AI_Transformation_Report.pdf",
            mime="application/pdf"
        )

    st.divider()

    with st.expander("🤖 View Detailed AI Strategy Report"):
        st.markdown(ai_report)
