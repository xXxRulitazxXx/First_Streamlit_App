import streamlit
import pandas

Lista_Frutas = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('Restaurante Rulitaz')
streamlit.header('Menú de desayuno')
streamlit.text('🥣 Omega 3 y avena con arándanos')
streamlit.text('🥗 Batido de col rizada, espinacas y rúcula')
streamlit.text('🐔 Huevo duro de gallinas camperas')

streamlit.header('🍌🥭 Prepara tu propio batido de frutas 🥝🍇')
# Ponemos una lista de selección aquí para que puedan elegir la fruta que quieran incluir 
streamlit.multiselect("Elige algunas frutas:", list(my_fruit_list.index)) 

# Muestra la tabla en la página.
streamlit.dataframe(Lista_Frutas)

