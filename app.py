import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.judge import evaluate_essay
from utils.kaggle_loader import load_kaggle_dataset

import streamlit as st
from utils.judge import evaluate_essay
from utils.kaggle_loader import load_kaggle_dataset

st.set_page_config(page_title="LLM as Judge", layout="centered")

st.title("🧑‍⚖️ LLM as a Judge – Essay Scoring")

# Load dataset once 
with st.spinner("Loading Kaggle dataset..."):
    df = load_kaggle_dataset()

st.success(f"Dataset loaded ✅ Total essays: {len(df)}")

essay = st.text_area("✍️ Enter your essay", height=250)

if st.button("Evaluate"):
    if essay.strip() == "":
        st.warning("Please write an essay first")
    else:
        with st.spinner("LLM is judging..."):
            result = evaluate_essay(essay)
            st.subheader("📊 LLM Judgment")
            st.code(result, language="json")
import streamlit as st
