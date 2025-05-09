import streamlit as st
import datetime
import os
import json

arquivos_salvos = 'veiculos_json'

def carregar_veiculos():
     if os.path.exists(arquivos_salvos):
         with open(arquivos_salvos, 'r', encoding= 'utf-8') as f:
             return json.load(f)
     return{}
         
def salvar_veiculos(veiculos):
    with open(arquivos_salvos, 'w', encoding= 'utf-8') as f:
        json.dump(veiculos, f, ensure_ascii=False, indent=4)


def criar_cadastro(data, cliente, telefone, placa, marca, modelo, ano, cor, km, resolver):
    return {
        'data': data,
        'cliente': cliente,
        'telefone': telefone,
        'placa': placa,
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'cor': cor,
        'km': km,
        'resolver': resolver
    }

        


def cadastro_veiculo():
    st.title('Cadastrar Veículo para Manutenção')
    st.write('Digite os dados do veiculo e do proprietário.')
    data_minima = datetime.date(1900,1,1)
    data_maxima = datetime.date(2100,1, 1)

    data = st.date_input('Data do cadastro?', format='DD/MM/YYYY',min_value=data_minima, max_value=data_maxima)
    cliente = st.text_input('Nome do cliente que veio com o veículo?')
    telefone = st.text_input('Telefone do cliente?')
    placa = st.text_input('Qual a placa do veículo ?')
    marca = st.text_input('Qual a marca do veículo ?')
    modelo = st.text_input('Qual o modelo do veículo ?')
    ano = st.number_input('Ano do veículo?', step=1, value=0, format='%d')
    cor = st.text_input('Qual a cor do veículo ?')
    km = st.number_input('Qual a quilometragem do veículo?', step=1, value=0, format='%d')
    resolver = st.text_area('Descreva o problema do veículo e o que deseja resolver:')


    st.write(f'{data} - {cliente} - {telefone} - {placa} - {marca} - {modelo} - {ano} - {cor} - {km} - {resolver}')


    if st.button('Cadastrar'):
        st.success('Veículo cadastrado')
        st.success('Os dados do veículo são:')
        st.write(f'{data} - {cliente} - {telefone} - {placa} - {marca} - {modelo} - {ano} - {cor} - {km} - {resolver}')

    

def consultar_veiculo():
    st.title('Consultar Veículos Cadastrados')
    st.write('Digite os dados do veiculo e do proprietário para consulta.')
    pass



def editar_veiculo():
    st.title('Editar Veículo Cadastrado')
    st.write('Digite os dados do veiculo e do proprietário para edição.')
    pass


def excluir_veiculo():
    st.title('Excluir Veículo Cadastrado')
    st.write('Digite os dados do veiculo e do proprietário para exclusão.')
    pass



#Menu lateral
st.sidebar.title('Menu')
opcao = st.sidebar.radio(
    'Selecione uma opção',
    ('Cadastrar Veículo', 'Consultar Veículo', 'Excluir Veículo',)
)


#Navegação entre as opções do menu lateral
if opcao == 'Cadastrar Veículo':
    cadastro_veiculo()
elif opcao == 'Consultar Veículo':
    consultar_veiculo()
elif opcao == 'Editar Veículo':
    editar_veiculo()
elif opcao == 'Excluir Veículo':
    excluir_veiculo()            
    

#Rodapé
st.sidebar.markdown('---')
st.sidebar.markdown('Desenvolvido por Leonardo Esmarjassi')
st.sidebar.markdown('Versão 1.0')
st.sidebar.markdown(f'Total de veículos cadastrados:')







    
