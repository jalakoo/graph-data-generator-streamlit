import streamlit as st
from tabs.instructions_tab import instructions_tab
from tabs.design_tab import design_tab
from tabs.generate_tab import generate_tab
from tabs.data_importer_tab import data_importer_tab
from tabs.config_tab import config_tab
from managers.n4j import reset
import logging
import sys

# SETUP
st.set_page_config(layout="wide")
logging.getLogger().setLevel(logging.DEBUG)
logging.info(f'App Started')

instructions_tab()

st.markdown("-------------")
# st.markdown("**⓪ CONFIG**")
with st.expander("Optional Configurations"):
    config_tab()

st.markdown("-------------")
st.markdown("**① DESIGN**")
design_tab()

st.markdown("-------------")
st.markdown("**② GENERATE**")
generate_tab()

st.markdown("-------------")
st.markdown("**③ IMPORT**")
c1, c2 = st.columns(2)
with c1: 
    use_neo = st.toggle("Auto Update Neo4j Instance", value = True, help="Automatically clear and re-upload mock data to Neo4j database instance specified in Configuration")
with c2:
    use_di = st.toggle("Use Data-Importer", value=False)
if use_neo:
    if st.button('Update'):
        uri = st.session_state.get("NEO4J_URI", None)
        user = st.session_state.get("NEO4J_USER", None)
        password = st.session_state.get("NEO4J_PASSWORD", None)
        reset(uri, user, password)
if use_di:
    data_importer_tab()