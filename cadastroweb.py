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
    st.write('Digite os dados do Veículo e do proprietário.')
    data_minima = datetime.date(1900,1,1)
    data_maxima = datetime.date(2100,1, 1)

    data = st.date_input('Data do cadastro ?', format='DD/MM/YYYY',min_value=data_minima, max_value=data_maxima)
    cliente = st.text_input('Nome do cliente que veio com o veículo?')
    telefone = st.text_input('Telefone do cliente?')
    placa = st.text_input('Qual a placa do veículo ?')
    marca = st.text_input('Qual a marca do veículo ?')
    modelo = st.text_input('Qual o modelo do veículo ?')
    ano = st.number_input('Ano do veículo?', step=1, value=0, format='%d')
    cor = st.text_input('Qual a cor do veículo ?')
    km = st.number_input('Qual a quilometragem do veículo?', step=1, value=0, format='%d')
    resolver = st.text_area('Descreva o problema do veículo e o que deseja resolver:')

    if st.button('Cadastrar'):
        veiculos = carregar_veiculos()
        veiculo = criar_cadastro(str(data), cliente, telefone, placa.upper(), marca, modelo, ano, cor, km, resolver)
        veiculos[placa.upper()] = veiculo  # Salva usando a placa como chave
        salvar_veiculos(veiculos)

        st.success('Veículo cadastrado com sucesso!')
        st.write(f'{data} - {cliente} - {telefone} - {placa} - {marca} - {modelo} - {ano} - {cor} - {km} - {resolver}')

def lista_veiculos():
    st.title('Lista de Veículos Cadastrados')
    st.write('Aqui estão os Veículos cadastrados:')

    veiculos = carregar_veiculos()

    if veiculos:
        for placa, veiculo in veiculos.items():
            with st.expander(f"Placa: {placa} | Cliente: {veiculo['cliente']}"):
                st.write(f"📅 Data: {veiculo['data']}")
                st.write(f"📞 Telefone: {veiculo['telefone']}")
                st.write(f"🚗 Marca: {veiculo['marca']}")
                st.write(f"📍 Modelo: {veiculo['modelo']}")
                st.write(f"🔢 Ano: {veiculo['ano']}")
                st.write(f"🎨 Cor: {veiculo['cor']}")
                st.write(f"📊 KM: {veiculo['km']}")
                st.write(f"🛠️ Problema: {veiculo['resolver']}")
    else:
        st.info('Nenhum veículo cadastrado até o momento.')

    


def consultar_veiculo():
    st.title('Consultar Veículos Cadastrados')
    st.write('Digite a placa do Veículo para consulta.')
    placa_consulta = st.text_input('Placa do Veículo:').upper()

    veiculos = carregar_veiculos()
    if placa_consulta:
        if placa_consulta in veiculos:
            veiculo = veiculos[placa_consulta]
            st.write(f"Data: {veiculo['data']}, Cliente: {veiculo['cliente']}, Telefone: {veiculo['telefone']}, Placa: {veiculo['placa']}, Marca: {veiculo['marca']}, Modelo: {veiculo['modelo']}, Ano: {veiculo['ano']}, Cor: {veiculo['cor']}, KM: {veiculo['km']}, Resolver: {veiculo['resolver']}")
        else:
            st.warning('Veículo não encontrado.')
    else:
        st.info('Digite uma placa para consultar.')
    
         

def editar_veiculo():
    st.title('Editar Veículo Cadastrado')
    st.write('Digite a placa do veículo que deseja editar.')

    placa_editar = st.text_input('Placa do Veículo:').upper()
    veiculos = carregar_veiculos()

    if placa_editar and placa_editar in veiculos:
        veiculo = veiculos[placa_editar]

        st.success('Veículo encontrado. Edite os dados abaixo.')

        data = st.date_input('Data do cadastro', value=datetime.datetime.strptime(veiculo['data'], "%Y-%m-%d").date())
        cliente = st.text_input('Nome do cliente', value=veiculo['cliente'])
        telefone = st.text_input('Telefone do cliente', value=veiculo['telefone'])
        marca = st.text_input('Marca do veículo', value=veiculo['marca'])
        modelo = st.text_input('Modelo do veículo', value=veiculo['modelo'])
        ano = st.number_input('Ano do veículo', value=int(veiculo['ano']), step=1, format='%d')
        cor = st.text_input('Cor do veículo', value=veiculo['cor'])
        km = st.number_input('Quilometragem do veículo', value=int(veiculo['km']), step=1, format='%d')
        resolver = st.text_area('Problema / Serviço a resolver', value=veiculo['resolver'])

        if st.button('Salvar alterações'):
            veiculos[placa_editar] = criar_cadastro(
                str(data), cliente, telefone, placa_editar, marca, modelo, ano, cor, km, resolver
            )
            salvar_veiculos(veiculos)
            st.success('Dados do veículo atualizados com sucesso!')
    elif placa_editar:
        st.warning('Veículo não encontrado.')




def excluir_veiculo():
    st.title('Excluir Veículo Cadastrado')
    st.write('Digite a placa do veículo que deseja excluir.')

    placa_excluir = st.text_input('Placa do Veículo:').upper()
    veiculos = carregar_veiculos()

    if placa_excluir and placa_excluir in veiculos:
        veiculo = veiculos[placa_excluir]

        st.warning('Atenção! Este veículo será excluído:')
        st.write(f"Data: {veiculo['data']}")
        st.write(f"Cliente: {veiculo['cliente']}")
        st.write(f"Telefone: {veiculo['telefone']}")
        st.write(f"Placa: {veiculo['placa']}")
        st.write(f"Marca: {veiculo['marca']}")
        st.write(f"Modelo: {veiculo['modelo']}")
        st.write(f"Ano: {veiculo['ano']}")
        st.write(f"Cor: {veiculo['cor']}")
        st.write(f"KM: {veiculo['km']}")
        st.write(f"Resolver: {veiculo['resolver']}")

        if st.button('Confirmar exclusão'):
            del veiculos[placa_excluir]
            salvar_veiculos(veiculos)
            st.success('Veículo excluído com sucesso!')
    elif placa_excluir:
        st.warning('Veículo não encontrado.')




#Menu lateral
st.sidebar.title('Menu')
opcao = st.sidebar.radio(
    'Selecione uma opção',
    ('Cadastrar Veículo', 'Consultar Veículo','Lista de Veículos', 'Editar Veículo', 'Excluir Veículo',)
)


#Navegação entre as opções do menu lateral
if opcao == 'Cadastrar Veículo':
    cadastro_veiculo()

elif opcao == 'Consultar Veículo':
    consultar_veiculo()

elif opcao == 'Lista de Veículos':
    lista_veiculos()

elif opcao == 'Editar Veículo':
    editar_veiculo()

elif opcao == 'Excluir Veículo':
    excluir_veiculo()            
    

#Rodapé
st.sidebar.markdown('---')
st.sidebar.markdown('Desenvolvido por Leonardo Esmarjassi')
st.sidebar.markdown('Versão 1.0')
st.sidebar.markdown(f'Total de veículos cadastrados:')







    
