import streamlit as st
from tabs.instructions_tab import instructions_tab
from tabs.design_tab import design_tab
from tabs.generate_tab import generate_tab
from tabs.data_importer_tab import data_importer_tab

# SETUP
st.set_page_config(layout="wide")

instructions_tab()

st.markdown("-------------")
st.markdown("**① DESIGN**")
design_tab()

st.markdown("-------------")
st.markdown("**② GENERATE**")
generate_tab()

st.markdown("-------------")
st.markdown("**③ IMPORT**")
data_importer_tab()