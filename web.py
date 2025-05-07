import streamlit as st
import datetime
st.title('Hello World')

st.write('Hello World! I am back!')

data_minima = datetime.date(1900,1,1)
data_maxima = datetime.date(2100,1, 1)

nome = st.text_input('Qual o seu Nome?')
idade = st.number_input('Idade?', step=1, value=0, format='%d')
Dtnasc = st.date_input('Nasc?', format='DD/MM/YYYY',min_value=data_minima   ,   max_value=data_maxima)


st.write(f'Olá {nome} de {idade} anos!')

st.write('Fale um pouco sobre você')
bio = st.text_area('')
