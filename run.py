import streamlit as st
from langchain_layer.orchestration.main_chain import final_chain

# --- Page Configuration ---
st.set_page_config(
    page_title="LangChain Enterprise AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    .main-header {
    font-size: 3.2rem;
    font-weight: 800;
    text-align: center;

    background: linear-gradient(90deg, #1B3C53, #4FA3D1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    }

    .sub-header {
        font-size: 1.2rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #E5E7EB;
    }
    .stButton > button {
        border-radius: 10px;
        width: 100%;
        background-color: #1B3C53;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
    }
    .stButton > button:hover {
        background-color: #234C6A;
        color: white;
    }
    .result-box {
    background-color: #1B3C53;
    padding: 1.5rem;
    border-radius: 10px;
    margin-top: 1rem;

    border-left: 6px solid;
    border-image: linear-gradient(to bottom, #4FA3D1, #D2C1B6) 1;
    box-shadow: 0 0 8px rgba(210,193,182,0.4);
    }

</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2083/2083256.png", width=80) 
    st.title("Enterprise AI")
    st.markdown("---")
    st.markdown("### 🚀 Capabilities")
    st.info(
        """
        - **Customer Risk Analysis**
        - **Financial Exposure Assessment**
        - **Automated Decision Support**
        """
    )
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.caption("Try asking about specific customers (e.g., *7795-CFOCW*) or general financial queries.")

# --- Main Content ---
st.markdown('<div class="main-header">Teleco Churn Intelligence System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Empowering business decisions with Autonomous AI Agents</div>', unsafe_allow_html=True)

# Layout for Input
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    query = st.text_input(
        "📝 Enter your business query:",
        placeholder="e.g., Make a decision for churn risk customer 7795-CFOCW",
        label_visibility="visible"
    )
    
    run_btn = st.button("🚀 Run Analysis")

# --- Logic & Results ---
if run_btn:
    if query.strip() == "":
        st.warning("⚠️ Please enter a query to proceed.")
    else:
        with st.spinner("🤖 AI Agent is analyzing data..."):
            try:
                # Invoke the chain
                result = final_chain.invoke({"query": query})
                
                st.markdown("---")
                st.subheader("📊 Analysis Results")
                
                # Display result in a styled box
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                
                # Verify logic: if result is a dictionary, we might want to parse it. 
                # For now, assuming string or printable object as per original code.
                
                st.success("Analysis executed successfully.")
                
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #9CA3AF; font-size: 0.8rem;'>"
    "Enterprise AI System • Powered by LangChain"
    "</div>", 
    unsafe_allow_html=True
)
