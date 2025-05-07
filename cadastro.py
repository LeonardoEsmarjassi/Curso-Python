import streamlit as st
import datetime
st.title('Cadastrar Veículo para Manutenção')
st.write('Digite os dados do veiculo e do proprietário.')


data_minima = datetime.date(1900,1,1)
data_maxima = datetime.date(2100,1, 1)


cliente = st.text_input('Nome do cliente que veio com o veículo?')
telefone = st.text_input('Telefone do cliente?')
placa = st.text_input('Qual a placa do veículo ?')
marca = st.text_input('Qual a marca do veículo ?')
modelo = st.text_input('Qual o modelo do veículo ?')
ano = st.number_input('Ano do veículo?', step=1, value=0, format='%d')
cor = st.text_input('Qual a cor do veículo ?')
km = st.number_input('Qual a quilometragem do veículo?', step=1, value=0, format='%d')
resolver = st.text_area('Descreva o problema do veículo e o que deseja resolver:')


st.write(f'{cliente} - {telefone} - {placa} - {marca} - {modelo} - {ano} - {cor} - {km} - {resolver}')


if st.button('Cadastrar'):
    st.success('Veículo cadastrado')
    st.success('Os dados do veículo são:')
    st.write(f'{cliente} - {telefone} - {placa} - {marca} - {modelo} - {ano} - {cor} - {km} - {resolver}')

    
