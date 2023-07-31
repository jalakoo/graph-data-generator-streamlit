import streamlit as st
from tabs.design_tab import design_tab
from tabs.generate_tab import generate_tab

# SETUP
st.set_page_config(layout="wide")

# Streamlit runs from top-to-bottom from tabs 1 through 8. This is essentially one giant single page app.  Earlier attempt to use Streamlit's multi-page app functionality resulted in an inconsistent state between pages.

t0, t1, t2, t3, t4, t5 = st.tabs([
    "⓪ Getting Started",
    "① Design",
    "② Generate",
    "③ Import",
    "④ Dashboard",
    "Ⓘ Info"
])

with t0:
    st.write('tbd')
with t1:
    design_tab()
with t2:
    generate_tab()
with t3:
    st.write('tbd')
with t4:
    st.write('tbd')
with t5:
    st.write('tbd')
