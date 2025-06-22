# src/style.py

import streamlit as st

def apply_custom_style():
    st.markdown("""
    <style>
        /* Main background and text */
        .main {
            background-color: #f8f9fa;
            color: #333333;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Sidebar */
        .sidebar .sidebar-content {
            background-color: #ffffff;
            color: #333333;
            border-right: 1px solid #ddd;
        }

        /* Inputs and dropdowns */
        .stTextInput textarea,
        .stTextArea textarea,
        .stSelectbox div[data-baseweb="select"] {
            background-color: #ffffff !important;
            color: #212529 !important;
            border: 1px solid #ced4da !important;
            border-radius: 6px;
        }

        .stSelectbox svg {
            fill: #495057 !important;
        }

        div[role="listbox"] div {
            background-color: #ffffff !important;
            color: #212529 !important;
        }

        /* Title */
        h1 {
            color: #495057;
            text-align: center;
            font-weight: 700;
            text-shadow: 0 0 2px rgba(173, 181, 189, 0.2);
        }

        /* Caption */
        .stCaption {
            color: #6c757d !important;
            text-align: center;
            font-style: italic;
            font-size: 0.9rem;
        }

        /* Button */
        button[kind="primary"] {
            background-color: #0d6efd !important;
            color: #fff !important;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(13, 110, 253, 0.3);
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        ::-webkit-scrollbar-thumb {
            background: #adb5bd;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

def show_sidebar_config():
    with st.sidebar:
        st.header("⚙️ Configuration")

        selected_model = st.selectbox(
            "🧠 Choose a DeepSeek Model",
            ["deepseek-r1:1.5b", "deepseek-r1:3b", "deepseek-r1:7b"],
            index=0,
            help="Choose the LLM size based on your system capabilities."
        )

        st.markdown("---")

        st.subheader("🧩 What This AI Can Do")
        st.markdown("""
        - 🔍 **Analyze & Improve Code**  
        - 🤖 **Generate Smart Code**   
        - 📘 **Explain Concepts Clearly**   
        - 🧠 **Design Efficient Solutions**   
        """, unsafe_allow_html=True)


        st.markdown("---")

        st.markdown(
            "🔗 **Built with:** "
            "[Ollama](https://ollama.ai) | "
            "[LangChain](https://python.langchain.com) | "
            "[DeepSeek](https://www.deepseek.com/en)"
        )

        return selected_model
