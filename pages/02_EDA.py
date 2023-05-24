import streamlit as st
import pandas as pd

from pathlib import Path

DATA_SRC = Path(__file__).parents[1].joinpath(
    "data",
    "cleaned_dataset.csv"
).resolve()

df = pd.read_csv(DATA_SRC)

st.title("EDA")
st.markdown("***")

st.sidebar.markdown("Índice de contenidos")

st.markdown("## Contenidos")