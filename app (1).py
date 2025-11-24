
import streamlit as st
import pdfplumber
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="FinSwarm Nexus: AI Auditor", layout="wide")

st.title("🤖 FinSwarm Nexus: AI Invoice Auditor")
st.markdown("### Upload a vendor invoice to detect fraud or errors instantly.")

# --- SIDEBAR (The Navigation) ---
st.sidebar.header("🔧 Control Panel")
app_mode = st.sidebar.selectbox("Choose Mode", ["Dashboard Overview", "AI Invoice Scanner"])

# ==========================================
# MODE 1: THE DASHBOARD (From Day 6)
# ==========================================
if app_mode == "Dashboard Overview":
    # (Simplified version of your previous dashboard)
    st.subheader("📊 Live Risk Monitor")
    
    # Fake data for demo (since we focus on the PDF part today)
    data = {'Customer': ['Alice', 'Bob', 'Charlie', 'David'],
            'Balance': [5000, -200, 12000, -50],
            'Risk': ['Low', 'High', 'Low', 'High']}
    df = pd.DataFrame(data)
    
    # Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Active Customers", "4")
    c2.metric("Total Risk Alerts", "2", delta="-2", delta_color="inverse")
    c3.metric("System Status", "Online 🟢")
    
    # Chart
    fig = px.bar(df, x='Customer', y='Balance', color='Risk', title="Customer Balance vs Risk")
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MODE 2: THE AI SCANNER (The Day 7 Magic)
# ==========================================
elif app_mode == "AI Invoice Scanner":
    st.subheader("📄 Upload Invoice for AI Analysis")
    
    # 1. THE UPLOADER
    uploaded_file = st.file_uploader("Drag and drop a PDF Invoice here", type="pdf")
    
    if uploaded_file:
        st.success("✅ File Uploaded! AI is reading...")
        
        # 2. THE AI READER (Day 4 Logic)
        with pdfplumber.open(uploaded_file) as pdf:
            page = pdf.pages[0]
            text = page.extract_text()
            
        # Display the Raw Text (Optional)
        with st.expander("See Raw Text extracted by AI"):
            st.text(text)
            
        # 3. THE LOGIC (Find the Money)
        # We look for "Total Due" or "$"
        extracted_amount = 0.0
        invoice_id = "Unknown"
        
        for line in text.split('\n'):
            if "$" in line:
                st.write(f"🔎 Found Money Line: *{line}*")
                # Simple logic: try to grab the number
                # (In a real app, we use Regex, but this works for simple PDFs)
            
            if "#" in line:
                invoice_id = line.split('#')[-1]

        # 4. THE DECISION (Risk Engine)
        st.markdown("---")
        st.subheader("🤖 AI Audit Verdict")
        
        col1, col2 = st.columns(2)
        col1.info(f"**Invoice ID Detected:** #{invoice_id}")
        
        # Fake logic for the demo (Real logic would check the amount against a database)
        if "High" in text or "Overdue" in text:
             col2.error("🚨 RISK STATUS: HIGH (Suspicious Keywords Found)")
        else:
             col2.success("✅ RISK STATUS: APPROVED (Looks clean)")
