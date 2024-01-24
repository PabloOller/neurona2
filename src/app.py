import streamlit as st
import pandas as pd
import numpy as np

st.image("images/neurona.jpg", width=360)

st.header("¡Hola neurona!")

arrPesos = [float(n) for n in st.text_input(f"Introduce los valores de los pesos separados por un espacio: ").split()]

arrEntradas = [float(n) for n in st.text_input(f"Introduce los valores de las entradas separados por un espacio: ").split()]

b = st.number_input("Introduzca el valor del sesgo")

if st.button("Calcular la salida", "b3"):
   if len(arrEntradas) == len(arrPesos):
      resultado = float(sum([a * b for a, b in zip(arrPesos, arrEntradas)])) + b
      st.text(f"La salida de la neurona es {resultado}")
   else:
      st.text(f"Tiene que haber el mismo valores de entradas y de pesos!")