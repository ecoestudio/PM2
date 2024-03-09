import pandas as pd
import streamlit as st
import time
from src.ui_helper import main

st.set_page_config(layout="wide", page_title='Playone助手')

if 'egg_smash_delay' not in st.session_state:
    st.session_state['egg_smash_delay'] = 0.1
if  'room_id' not in st.session_state:
    st.session_state['room_id'] = ""

        
if __name__ == "__main__":
    main()
