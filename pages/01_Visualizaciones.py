import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from pathlib import Path

DATA_SRC = Path(__file__).parents[1].joinpath(
    "data",
    "cleaned_dataset.csv"
).resolve()

df = pd.read_csv(DATA_SRC)

st.title("Visualizaciones")
st.markdown("***")

st.sidebar.markdown("Índice de contenidos")

st.markdown("## Contenidos")
st.write("""
Gráficos usados durante el análisis del KPI principal de este
proyecto:

- Reducir en 5% la tasa de mortalidad a nivel anual, siendo el
número de fallecidos en los accidentes aéreos respecto al total
de personas en los vuelos involucrados.
""")

if st.checkbox("DataFrame usado"):
    st.dataframe(df)

if st.checkbox("Descripción estadística del dataset"):
    st.write(df.describe())

st.markdown("### Años con mayor mortalidad")
anios_mortalidad = st.slider(
    "Últimos N años a visualizar:",
    5,
    20,
    10
)

fig_top_mortalidad = plt.figure(figsize=(10, 6))
df.groupby("año")["total fallecidos"].sum().nlargest(anios_mortalidad).plot(
    kind="barh",
    title=f"Top {anios_mortalidad} años con mayor cantidad de fallecidos",
    xlabel="Cantidad",
    ylabel="Año"
)
st.pyplot(fig_top_mortalidad)

st.markdown("### Total fallecidos anuales")
anios_total = st.slider(
    "N años a visualizar:",
    5,
    20,
    10
)

fig_mortalidad_anual = plt.figure(figsize=(10, 6))
df.groupby("año")["total fallecidos"].sum().tail(anios_total).plot(
    kind="line",
    title=f"Total fallecidos anuales últimos {anios_total} años",
    grid=True,
    xlabel="Año",
    ylabel="Cantidad",
    xticks=df.groupby("año")["total fallecidos"].sum().tail(anios_total).index
)
st.pyplot(fig_mortalidad_anual)

st.markdown("### Promedio tasa mortalidad")

df["tasa mortalidad"] = df["total fallecidos"].div(df["total personas a bordo"]).mul(100)

anios_promedio = st.slider(
    "Promedio mortalidad en N años",
    5,
    20,
    10
)
fig_promedio_mortalidad = plt.figure(figsize=(10, 6))
tasa_mortalidad_anual = df.groupby("año")["tasa mortalidad"].mean().round(2)
tasa_mortalidad_anual.tail(anios_promedio).plot(
    figsize=(10, 6),
    kind="line",
    title=f"Promedio tasa mortalidad últimos {anios_promedio} años",
    grid=True,
    xlabel="Año",
    ylabel="Valor promedio",
    xticks=tasa_mortalidad_anual.tail(anios_promedio).index
)
st.pyplot(fig_promedio_mortalidad)

st.markdown("### Cambio porcentual promedio mortalidad")

anios_porcent = st.slider(
    "Cambio porcentual promedio mortalidad en N años",
    5,
    20,
    10
)

fig_porcent_mortal = plt.figure(figsize=(10, 6))
porcent_tasa_mortalidad = tasa_mortalidad_anual.pct_change().round(2).fillna(0.0)
porcent_tasa_mortalidad.tail(anios_porcent).plot(
    kind="line",
    title="Cambio porcentual de tasa de mortalidad anual",
    grid=True,
    xlabel="Año",
    ylabel="Porcentaje",
    xticks=porcent_tasa_mortalidad.tail(anios_porcent).index
)
st.pyplot(fig_porcent_mortal)