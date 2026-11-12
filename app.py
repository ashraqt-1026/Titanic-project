import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px
from utils.data import load_data
from utils.config import COLORS, ORDERS
from utils.figures import plot_family_size, plot_outcome

st.title("my titanic App")
st.image("utils/titanic.jpeg")

df = load_data()

classes = st.multiselect("select class", df["class"].unique(), default = df["class"].unique())
gender = st.radio("select class", df['sex'].unique(), horizontal = True)

data = df[(df["class"].isin(classes)) & (df["sex"] == gender)]

show_data = st.checkbox("show sample data")
if show_data:
    st.dataframe(df, hide_index=True)
c1, c2 = st.columns(2)
with c1:
    fig = plot_family_size(data)
    st.plotly_chart(fig)
with c2:
    fig = plot_outcome(data)
    st.plotly_chart(fig)
