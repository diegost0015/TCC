from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTableView, QTableWidget, QPushButton
from PyQt5 import uic
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "realizar_orcamento"
    )

def chama_tela_orcamento_cliente():
    tela_orcamento_cliente.show()

def realizar_orcamento():
    linha1 = tela_orcamento_cliente.lineEdit_desc.text()
    linha2 = tela_orcamento_cliente.spinBox_uni.text()
    linha3 = tela_orcamento_cliente.spinBox_qtd.text()
    linha4 = tela_orcamento_cliente.lineEdit_lista.text()
    linha5 = tela_orcamento_cliente.spinBox_desconto.text()
    linha6 = tela_orcamento_cliente.lineEdit_unid.text()
    linha7 = tela_orcamento_cliente.lineEdit_total.text()
    linha8 = tela_orcamento_cliente.lineEdit_frete.text()

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO realizar_orcamento (Descricao_Produto, Unidade, Qtd, Preco_lista, Desconto, Preco_uni, Preco_total, Frete) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1), int(linha2), int(linha3), float(linha4), int(linha5), float(linha6), float(linha7), float(linha8))
    cursor.execute(comando_SQL, dados)
    banco.commit()

def visualizar_orcamentos():
    pass

app = QtWidgets([])
menu = uic.loadUi("Menu.ui")
menu.orcamento_cliente.triggered.connect(chama_tela_orcamento_cliente)

tela_orcamento_cliente = uic.loadUi("Realizar_Orcamento_Cliente_Empresa.ui")
tela_orcamento_cliente.show()
app.exec()

"""
Feito:

Interface da realização e visualização de orçamento.
Código fonte .py para execução das funcionalidades.
Criação da tabala no banco "realizar orçamento".
Integração com o banco "realizar orçamento".

Falta:

Condições para o botão de calcular orçamento e o botão criar orçamento.
Necessário da criação de função para visualização de orçamentos.
Necessário a criação de função para pesquisa na descrição do produto e a integração com a tabela de produtos.
"""