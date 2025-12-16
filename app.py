import pandas as pd
import plotly.express as px
import streamlit as st

# --- 1. Carga de datos ---
car_data = pd.read_csv('vehicles_us.csv') 

# --- 2. Título y Encabezado ---
st.header('Análisis de Vehículos Usados - Sprint 7')
st.write("""
Esta aplicación permite analizar un conjunto de datos de anuncios de venta de coches.
Selecciona las opciones a continuación para visualizar la información.
""")

# --- 3. Botón para Histograma (Instrucción básica + Desafío Checkbox) ---
# Usamos checkbox porque mantiene el gráfico en pantalla
build_histogram = st.checkbox('Construir un histograma (Odómetro)')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    
    st.write('Mostrando la distribución del kilometraje de los vehículos:')
    
    # Crear el gráfico
    # Usamos plotly.express que es más moderno y rápido de escribir que graph_objects
    fig = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

# --- 4. Botón para Gráfico de Dispersión (Instrucción básica + Desafío Checkbox) ---
build_scatter = st.checkbox('Construir un gráfico de dispersión (Precio vs Odómetro)')

if build_scatter:
    st.write('Construir un gráfico de dispersión para las columnas odómetro y precio')
    
    st.write('Mostrando la relación entre el precio y el kilometraje:')
    
    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Odómetro")
    
    st.plotly_chart(fig_scatter, use_container_width=True)