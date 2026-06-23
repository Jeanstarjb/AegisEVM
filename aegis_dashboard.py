import streamlit as st
import subprocess
import os
import tempfile
from pathlib import Path

# --- Configuration ---
st.set_page_config(
    page_title="AegisEVM Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for dark hacker aesthetic
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stButton>button {
        background-color: #238636;
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #2ea043;
    }
    .console-output {
        font-family: 'Courier New', Courier, monospace;
        background-color: #010409;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #30363d;
        color: #00ff00;
        white-space: pre-wrap;
    }
    .stAlert {
        background-color: #161b22;
        border: 1px solid #30363d;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Ethereum_logo_2014.svg/1257px-Ethereum_logo_2014.svg.png", width=50)
    st.title("🛡️ AegisEVM")
    st.markdown("### The Enforcer")
    st.markdown("Upload a Solidity smart contract to run a deep symbolic execution analysis.")
    st.divider()
    tx_depth = st.slider("Max Transaction Depth", min_value=1, max_value=10, value=3)
    timeout = st.slider("Execution Timeout (s)", min_value=10, max_value=600, value=60)

# --- Main Area ---
st.title("Smart Contract Auditor")
st.markdown("> **Code is law. Aegis is the enforcer.**")

uploaded_file = st.file_uploader("Upload Solidity File (.sol)", type=['sol'])

if uploaded_file is not None:
    st.success(f"Loaded `{uploaded_file.name}` successfully.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Contract Source")
        source_code = uploaded_file.getvalue().decode("utf-8")
        st.code(source_code, language='solidity')
        
    with col2:
        st.markdown("### Audit Execution")
        
        if st.button("🚀 Launch Analysis", use_container_width=True):
            with st.spinner("Initializing Aegis Engine..."):
                # Save uploaded file to temp location
                with tempfile.NamedTemporaryFile(delete=False, suffix=".sol") as tmp:
                    tmp.write(uploaded_file.getvalue())
                    tmp_path = tmp.name
                
                try:
                    # Run mythril via subprocess
                    cmd = [
                        "myth", "analyze", tmp_path,
                        "-t", str(tx_depth),
                        "--execution-timeout", str(timeout)
                    ]
                    
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    
                    st.markdown("#### Raw Output Log")
                    
                    output_text = result.stdout if result.stdout else result.stderr
                    
                    if "The analysis was completed successfully. No issues were detected." in output_text:
                        st.balloons()
                        st.markdown(f'<div class="console-output" style="color: #00ff00;">{output_text}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="console-output" style="color: #ff4444;">{output_text}</div>', unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error(f"Execution failed: {str(e)}")
                finally:
                    os.unlink(tmp_path)
