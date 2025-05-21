import streamlit as st
import datetime
import os
import json

arquivos_salvos = 'veiculos_json'

def carregar_veiculos():
    if os.path.exists(arquivos_salvos):
        with open(arquivos_salvos, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def salvar_veiculos(veiculos):
    with open(arquivos_salvos, 'w', encoding='utf-8') as f:
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
    st.title('📋 Cadastro de Veículo para Manutenção')
    st.markdown('Preencha os dados abaixo para registrar um novo veículo. 🚘')

    data_minima = datetime.date(1900,1,1)
    data_maxima = datetime.date(2100,1,1)

    data = st.date_input('📅 Data do cadastro:', format='DD/MM/YYYY', min_value=data_minima, max_value=data_maxima)
    cliente = st.text_input('👤 Nome do cliente:')
    telefone = st.text_input('📞 Telefone para contato:')
    placa = st.text_input('🔤 Placa do veículo:')
    marca = st.text_input('🏷️ Marca:')
    modelo = st.text_input('📍 Modelo:')
    ano = st.number_input('📆 Ano do veículo:', step=1, value=0, format='%d')
    cor = st.text_input('🎨 Cor:')
    km = st.number_input('📊 Quilometragem:', step=1, value=0, format='%d')
    resolver = st.text_area('🛠️ Descreva o problema ou serviço desejado:')

    if st.button('✅ Cadastrar'):
        veiculos = carregar_veiculos()
        veiculo = criar_cadastro(str(data), cliente, telefone, placa.upper(), marca, modelo, ano, cor, km, resolver)
        veiculos[placa.upper()] = veiculo
        salvar_veiculos(veiculos)

        st.success('🎉 Veículo cadastrado com sucesso!')
        st.write(f'**Resumo:**\n{data} | {cliente} | {telefone} | {placa} | {marca} | {modelo} | {ano} | {cor} | {km} | {resolver}')

def lista_veiculos():
    st.title('📑 Lista de Veículos Cadastrados')
    st.markdown('Veja abaixo todos os veículos já registrados na oficina. 🛠️')

    veiculos = carregar_veiculos()

    if veiculos:
        for placa, veiculo in veiculos.items():
            with st.expander(f"📌 {placa} | Cliente: {veiculo['cliente']}"):
                st.write(f"📅 Data: {veiculo['data']}")
                st.write(f"📞 Telefone: {veiculo['telefone']}")
                st.write(f"🚗 Marca: {veiculo['marca']}")
                st.write(f"📍 Modelo: {veiculo['modelo']}")
                st.write(f"🔢 Ano: {veiculo['ano']}")
                st.write(f"🎨 Cor: {veiculo['cor']}")
                st.write(f"📊 KM: {veiculo['km']}")
                st.write(f"🛠️ Problema: {veiculo['resolver']}")
    else:
        st.info('🚫 Nenhum veículo cadastrado ainda.')

def consultar_veiculo():
    st.title('🔍 Consultar Veículo')
    st.markdown('Digite a **placa do veículo** ao lado para visualizar os dados.')

    placa_consulta = st.sidebar.text_input('🔎 Placa:').upper()
    veiculos = carregar_veiculos()

    if placa_consulta:
        if placa_consulta in veiculos:
            veiculo = veiculos[placa_consulta]
            st.success('✅ Veículo encontrado!')
            st.write(f"📅 Data: {veiculo['data']}")
            st.write(f"👤 Cliente: {veiculo['cliente']}")
            st.write(f"📞 Telefone: {veiculo['telefone']}")
            st.write(f"🚗 Marca: {veiculo['marca']}")
            st.write(f"📍 Modelo: {veiculo['modelo']}")
            st.write(f"🔢 Ano: {veiculo['ano']}")
            st.write(f"🎨 Cor: {veiculo['cor']}")
            st.write(f"📊 KM: {veiculo['km']}")
            st.write(f"🛠️ Problema: {veiculo['resolver']}")
        else:
            st.warning('⚠️ Veículo não encontrado.')
    else:
        st.info('💡 Dica: digite a placa ao lado para iniciar a consulta.')

def editar_veiculo():
    st.title('✏️ Editar Veículo')
    st.markdown('Digite a **placa** ao lado para alterar os dados do veículo.')

    placa_editar = st.sidebar.text_input('🔤 Placa:').upper()
    veiculos = carregar_veiculos()

    if placa_editar and placa_editar in veiculos:
        veiculo = veiculos[placa_editar]
        st.success('🟢 Veículo localizado! Altere os dados ao lado.')

        data = st.sidebar.date_input('📅 Data do cadastro:', value=datetime.datetime.strptime(veiculo['data'], "%Y-%m-%d").date())
        cliente = st.sidebar.text_input('👤 Nome do cliente:', value=veiculo['cliente'])
        telefone = st.sidebar.text_input('📞 Telefone:', value=veiculo['telefone'])
        marca = st.sidebar.text_input('🏷️ Marca:', value=veiculo['marca'])
        modelo = st.sidebar.text_input('📍 Modelo:', value=veiculo['modelo'])
        ano = st.sidebar.number_input('📆 Ano:', value=int(veiculo['ano']), step=1, format='%d')
        cor = st.sidebar.text_input('🎨 Cor:', value=veiculo['cor'])
        km = st.sidebar.number_input('📊 Quilometragem:', value=int(veiculo['km']), step=1, format='%d')
        resolver = st.sidebar.text_area('🛠️ Serviço a realizar:', value=veiculo['resolver'])

        if st.sidebar.button('💾 Salvar alterações'):
            veiculos[placa_editar] = criar_cadastro(str(data), cliente, telefone, placa_editar, marca, modelo, ano, cor, km, resolver)
            salvar_veiculos(veiculos)
            st.success('✅ Dados atualizados com sucesso!')
    elif placa_editar:
        st.warning('🚫 Veículo não encontrado.')

def excluir_veiculo():
    st.title('🗑️ Excluir Veículo')
    st.markdown('Digite a **placa** ao lado para remover o veículo do sistema.')

    placa_excluir = st.sidebar.text_input('🔤 Placa:').upper()
    veiculos = carregar_veiculos()

    if placa_excluir and placa_excluir in veiculos:
        veiculo = veiculos[placa_excluir]
        st.warning('⚠️ Atenção! Os dados abaixo serão excluídos:')
        st.write(f"📅 Data: {veiculo['data']}")
        st.write(f"👤 Cliente: {veiculo['cliente']}")
        st.write(f"📞 Telefone: {veiculo['telefone']}")
        st.write(f"🚗 Marca: {veiculo['marca']}")
        st.write(f"📍 Modelo: {veiculo['modelo']}")
        st.write(f"🔢 Ano: {veiculo['ano']}")
        st.write(f"🎨 Cor: {veiculo['cor']}")
        st.write(f"📊 KM: {veiculo['km']}")
        st.write(f"🛠️ Problema: {veiculo['resolver']}")

        if st.sidebar.button('✅ Confirmar exclusão'):
            del veiculos[placa_excluir]
            salvar_veiculos(veiculos)
            st.success('🗑️ Veículo excluído com sucesso!')
    elif placa_excluir:
        st.warning('🚫 Veículo não encontrado.')

# MENU LATERAL
st.sidebar.title('📚 Menu da Oficina')
opcao = st.sidebar.radio(
    '🚦 Selecione uma opção:',
    ('Cadastrar Veículo', 'Consultar Veículo', 'Lista de Veículos', 'Editar Veículo', 'Excluir Veículo')
)

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

st.sidebar.markdown('---')
st.sidebar.markdown('👨‍💻 Desenvolvido por **Leonardo Esmarjassi**')
st.sidebar.markdown('📦 Versão 1.0')
st.sidebar.markdown(f'Total de veículos cadastrados: {len(carregar_veiculos())}')
