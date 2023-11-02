import streamlit
import pandas
import requests

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
streamlit.header("FruityVice Advice!")
#streamlit.text(fruityvice_response.json()) --Se pide que se borre esta línea
fruit_choice = streamlit.text_input('De que fruta quieres más información?','Kiwi')
streamlit.write('El usuario ingresó: ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
