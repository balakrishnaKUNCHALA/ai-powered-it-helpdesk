
import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env", override=True)
api_key = os.getenv("GEMINI_API_KEY")
gemini_client = genai.Client(api_key=api_key) if api_key else None
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
gemini_client = genai.Client(api_key=api_key) if api_key else None


def get_gemini_troubleshooting(issue, category):
    if gemini_client is None:
        return "Gemini API key is missing. Check your .env file."

    try:
        response = gemini_client.models.generate_content(
            model="gemini-3.8-flash",
            contents=(
                "You are an IT helpdesk assistant. Give 3 safe, "
                "simple troubleshooting steps. Do not request passwords. "
                f"\nIssue category: {category}"
                f"\nUser issue: {issue}"
            ),
        )
        return response.text or "No response received from Gemini."
    except Exception as exc:
        return f"Gemini request failed: {exc}"


import pandas as pd
from datetime import datetime
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="AI IT Helpdesk",
    page_icon="🛠️",
    layout="wide"
)

if "tickets" not in st.session_state:
    st.session_state.tickets = []

st.title("🛠️ AI-Powered IT Helpdesk")
st.write("Report IT issues, get troubleshooting suggestions, and track tickets.")

# Sidebar: Create ticket
with st.sidebar:
    st.header("📩 Report an Issue")

    name = st.text_input("Your Name")

    category = st.selectbox(
        "Issue Category",
        ["Hardware", "Network", "Software", "Account Access"]
    )

    priority = st.selectbox(
        "Priority",
        ["Low", "Medium", "High"]
    )

    description = st.text_area("Describe Your Issue")

    if st.button("Submit Ticket", type="primary"):
        if name.strip() and description.strip():
            ticket = {
                "Ticket ID": f"IT-{len(st.session_state.tickets) + 1:03d}",
                "Name": name.strip(),
                "Category": category,
                "Priority": priority,
                "Description": description.strip(),
                "Status": "Open",
                "Created At": datetime.now().strftime("%Y-%m-%d %H:%M")
            }

            st.session_state.tickets.append(ticket)
            st.success(f"Ticket {ticket['Ticket ID']} created!")
        else:
            st.warning("Please enter your name and issue description.")


# AI Troubleshooting Assistant
st.header("💡 AI Troubleshooting Assistant")

st.write("Describe your IT issue to get AI-powered troubleshooting steps.")

ai_category = st.selectbox(
    "Select an issue category",
    ["Hardware", "Network", "Software", "Account Access"],
    key="ai_category"
)

ai_issue = st.text_area(
    "Describe your IT problem",
    placeholder="Example: My laptop is connected to Wi-Fi, but the internet is not working.",
    key="ai_issue"
)

if st.button("Get AI Troubleshooting", type="primary"):
    if ai_issue.strip():
        with st.spinner("AI is analysing your issue..."):
            ai_result = get_gemini_troubleshooting(
                ai_issue.strip(), ai_category
            )
        st.subheader("AI Suggestions")
        st.markdown(ai_result)
    else:
        st.warning("Please describe your IT problem first.")


st.divider()

# Dashboard
st.header("📊 Helpdesk Dashboard")


tickets = st.session_state.tickets

total = len(tickets)
open_count = sum(t["Status"] == "Open" for t in tickets)
high_count = sum(t["Priority"] == "High" for t in tickets)

col1, col2, col3 = st.columns(3)

col1.metric("Total Tickets", total)
col2.metric("Open Tickets", open_count)
col3.metric("High Priority", high_count)

if tickets:
    df = pd.DataFrame(tickets)

    st.subheader("🎫 All Support Tickets")
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.subheader("Update Ticket Status")

    ticket_ids = [ticket["Ticket ID"] for ticket in tickets]

    selected_ticket = st.selectbox(
        "Choose Ticket ID",
        ticket_ids
    )

    new_status = st.selectbox(
        "Choose New Status",
        ["Open", "In Progress", "Resolved"]
    )

    if st.button("Update Status"):
        for ticket in st.session_state.tickets:
            if ticket["Ticket ID"] == selected_ticket:
                ticket["Status"] = new_status

        st.success(f"{selected_ticket} status updated!")
        st.rerun()

    csv_data = pd.DataFrame(
        st.session_state.tickets
    ).to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Tickets as CSV",
        data=csv_data,
        file_name="helpdesk_tickets.csv",
        mime="text/csv"
    )

else:
    st.info("No tickets available. Submit your first issue using the sidebar.")

st.divider()
st.caption("IT Helpdesk Automation — Project Prototype")
