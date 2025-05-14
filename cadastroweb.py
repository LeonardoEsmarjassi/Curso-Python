import streamlit as st
import datetime
import os
import json

# Nome do arquivo onde os dados dos veículos serão armazenados em formato JSON
arquivos_salvos = 'veiculos_json'

# Função para carregar os veículos salvos no arquivo JSON
def carregar_veiculos():
    if os.path.exists(arquivos_salvos):
        with open(arquivos_salvos, 'r', encoding='utf-8') as f:
            return json.load(f)  # Retorna o dicionário de veículos
    return {}  # Se o arquivo não existir, retorna um dicionário vazio

# Função para salvar os dados dos veículos no arquivo JSON
def salvar_veiculos(veiculos):
    with open(arquivos_salvos, 'w', encoding='utf-8') as f:
        json.dump(veiculos, f, ensure_ascii=False, indent=4)  # Salva formatado com identação

# Função que cria o dicionário com os dados do veículo
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

# Função principal para cadastrar um novo veículo
def cadastro_veiculo():
    st.title('Cadastrar Veículo para Manutenção')  # Título da página
    st.write('Digite os dados do Veículo e do proprietário.')  # Instrução ao usuário
    
    # Define limites para a data
    data_minima = datetime.date(1900,1,1)
    data_maxima = datetime.date(2100,1,1)

    # Campos de entrada
    data = st.date_input('Data do cadastro ?', format='DD/MM/YYYY', min_value=data_minima, max_value=data_maxima)
    cliente = st.text_input('Nome do cliente que veio com o veículo?')
    telefone = st.text_input('Telefone do cliente?')
    placa = st.text_input('Qual a placa do veículo ?')
    marca = st.text_input('Qual a marca do veículo ?')
    modelo = st.text_input('Qual o modelo do veículo ?')
    ano = st.number_input('Ano do veículo?', step=1, value=0, format='%d')
    cor = st.text_input('Qual a cor do veículo ?')
    km = st.number_input('Qual a quilometragem do veículo?', step=1, value=0, format='%d')
    resolver = st.text_area('Descreva o problema do veículo e o que deseja resolver:')

    # Botão para cadastrar
    if st.button('Cadastrar'):
        veiculos = carregar_veiculos()  # Carrega veículos já cadastrados
        veiculo = criar_cadastro(str(data), cliente, telefone, placa.upper(), marca, modelo, ano, cor, km, resolver)
        veiculos[placa.upper()] = veiculo  # Usa a placa (em maiúsculo) como chave
        salvar_veiculos(veiculos)  # Salva os dados

        st.success('Veículo cadastrado com sucesso!')
        st.write(f'{data} - {cliente} - {telefone} - {placa} - {marca} - {modelo} - {ano} - {cor} - {km} - {resolver}')

# Função para listar todos os veículos cadastrados
def lista_veiculos():
    st.title('Lista de Veículos Cadastrados')
    st.write('Aqui estão os Veículos cadastrados:')

    veiculos = carregar_veiculos()  # Carrega os dados

    # Se houver veículos cadastrados, exibe cada um
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

# Função para consultar um veículo pela placa
def consultar_veiculo():
    st.title('Consultar Veículos Cadastrados')
    st.write('Digite a placa do Veículo para consulta.')
    placa_consulta = st.text_input('Placa do Veículo:').upper()

    veiculos = carregar_veiculos()
    if placa_consulta:
        if placa_consulta in veiculos:
            veiculo = veiculos[placa_consulta]
            # Exibe os dados encontrados
            st.write(f"Data: {veiculo['data']}, Cliente: {veiculo['cliente']}, Telefone: {veiculo['telefone']}, Placa: {veiculo['placa']}, Marca: {veiculo['marca']}, Modelo: {veiculo['modelo']}, Ano: {veiculo['ano']}, Cor: {veiculo['cor']}, KM: {veiculo['km']}, Resolver: {veiculo['resolver']}")
        else:
            st.warning('Veículo não encontrado.')
    else:
        st.info('Digite uma placa para consultar.')

# Função para editar os dados de um veículo
def editar_veiculo():
    st.title('Editar Veículo Cadastrado')
    st.write('Digite a placa do veículo que deseja editar.')

    placa_editar = st.text_input('Placa do Veículo:').upper()
    veiculos = carregar_veiculos()

    if placa_editar and placa_editar in veiculos:
        veiculo = veiculos[placa_editar]

        st.success('Veículo encontrado. Edite os dados abaixo.')

        # Campos preenchidos com os dados já existentes
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
            # Atualiza os dados
            veiculos[placa_editar] = criar_cadastro(
                str(data), cliente, telefone, placa_editar, marca, modelo, ano, cor, km, resolver
            )
            salvar_veiculos(veiculos)  # Salva os dados atualizados
            st.success('Dados do veículo atualizados com sucesso!')
    elif placa_editar:
        st.warning('Veículo não encontrado.')

# Função para excluir um veículo cadastrado
def excluir_veiculo():
    st.title('Excluir Veículo Cadastrado')
    st.write('Digite a placa do veículo que deseja excluir.')

    placa_excluir = st.text_input('Placa do Veículo:').upper()
    veiculos = carregar_veiculos()

    if placa_excluir and placa_excluir in veiculos:
        veiculo = veiculos[placa_excluir]

        # Mostra os dados do veículo antes de excluir
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

        # Botão de confirmação da exclusão
        if st.button('Confirmar exclusão'):
            del veiculos[placa_excluir]  # Remove o veículo do dicionário
            salvar_veiculos(veiculos)  # Salva os dados
            st.success('Veículo excluído com sucesso!')
    elif placa_excluir:
        st.warning('Veículo não encontrado.')

# Menu lateral com as opções
st.sidebar.title('Menu')
opcao = st.sidebar.radio(
    'Selecione uma opção',
    ('Cadastrar Veículo', 'Consultar Veículo','Lista de Veículos', 'Editar Veículo', 'Excluir Veículo',)
)

# Executa a função escolhida no menu
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

# Rodapé do menu lateral
st.sidebar.markdown('---')
st.sidebar.markdown('Desenvolvido por Leonardo Esmarjassi')
st.sidebar.markdown('Versão 1.0')
