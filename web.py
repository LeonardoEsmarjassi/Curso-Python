import streamlit as st  

st.title('Hello world !')

st.write('Hello world ! I am back !')


nome = st.text_input('Qual é o seu nome ?')
idade = st.number_input('Idade ?', step=1, value=0, format='%d')
dtnasc = st.date_input('Data de nascimento ?')

st.write(f'Olá {nome}, você tem {idade} anos !')

st.write('Fale um pouco sobre você')
bio = st.text_area('')