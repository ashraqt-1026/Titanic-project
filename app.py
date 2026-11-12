import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

st.title("my titanic App")
st.image("utils/titanic.jpeg")
df = pd.read_csv("data/titanic.csv")
df.columns = df.columns.str.lower()
df["class"] = df["pclass"].map({1: "First", 2: "Second", 3: "Third"})
df["survival"] = df["survived"].map({0: "Died", 1: "Survived"})
df["port"] = df["embarked"].map({"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"})
df["family_size"] = df["sibsp"] + df["parch"] + 1
df["title"] = df["name"].str.extract(r",\s*([^\.]+)\.", expand=False)
df["age_group"] = pd.cut(df["age"], [0, 12, 18, 35, 60, 80],
                         labels=["child", "teen", "young adult", "adult", "senior"])

ORDERS = {"class": ["First", "Second", "Third"], "survival": ["Died", "Survived"],
          "age_group": ["child", "teen", "young adult", "adult", "senior"]}
COLORS = {"Died": "#D95D4A", "Survived": "#0F766E"}


classes = st.multiselect("select class", df["class"].unique(), default = df["class"].unique())
gender = st.radio("select class", df['sex'].unique(), horizontal = True)

data = df[(df["class"].isin(classes)) & (df["sex"] == gender)]

show_data = st.checkbox("show sample data")
if show_data:
    st.dataframe(df, hide_index=True)
c1, c2 = st.columns(2)
with c1:
    fig = px.histogram(data, x = 'family_size')
    st.plotly_chart(fig)
with c2:
    outcome = data['survived'].value_counts()
    fig2 = px.pie(names =['died', 'survived'], values = outcome.values,  hole=0.4)
    st.plotly_chart(fig2)
