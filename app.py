import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title('DATA ANALYSIS MINI PROJECT')
st.markdown('This is a mini project for data analysis using streamlit and plotly')
st.subheader('ADMISSION IN UNIVERSITIES')
# Load data
df = pd.read_csv('dataset.csv')
# Show dataset
if st.checkbox('Show Dataset'):
    st.write(df)
