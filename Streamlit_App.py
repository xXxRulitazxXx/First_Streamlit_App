import streamlit
import pandas
import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

Lista_Frutas = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
Lista_Frutas = Lista_Frutas.set_index('Fruit') #Se coloca en inglés ya que en el recurso que se llama la Cabecera se llama de esa manera.

streamlit.title('Restaurante Rulitaz')
streamlit.header('Menú de desayuno')
streamlit.text('🥣 Omega 3 y avena con arándanos')
streamlit.text('🥗 Batido de col rizada, espinacas y rúcula')
streamlit.text('🐔 Huevo duro de gallinas camperas')

streamlit.header('🍌🥭 Prepara tu propio batido de frutas 🥝🍇')
# Ponemos una lista de selección aquí para que puedan elegir la fruta que quieran incluir 
Frutas_Seleccionadas = streamlit.multiselect("Elige algunas frutas:", list(Lista_Frutas.index),['Avocado', 'Strawberries'])
Frutas_A_Mostrar = Lista_Frutas.loc[Frutas_Seleccionadas]

# Muestra la tabla en la página.
streamlit.dataframe(Frutas_A_Mostrar)

#Nueva linea de Requests
streamlit.header("¡Enterate de Esto!")
streamlit.text(fruityvice_response.json())

