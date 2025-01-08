import pandas as pd
import numpy as np
import streamlit as st
import joblib
import matplotlib

nama = st.text_area("input nama anda", max_chars=100)
st.write(nama)