from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTableView, QTableWidget, QPushButton
from PyQt5 import uic
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "teste"

)



def chama_tela_cadastro(self):
    tela_cadastro.show()

def chama_tela_estoque():
    tela_estoque.show()
    lista = [("Editar"),("Deletar")]

    cursor = banco.cursor()
    comando_SQL = "SELECT *FROM  produtos"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()
    print(dados)

    tela_estoque.tableWidget.setRowCount(len(dados))
    tela_estoque.tableWidget.setColumnCount(10)

    for i in range(0, len(dados)):
        for j in range(0, 8):
            tela_estoque.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))
            

def cadastro():
    linha1 = tela_cadastro.lineEdit_2.text()
    linha2 = tela_cadastro.lineEdit_3.text()
    linha3 = tela_cadastro.lineEdit_4.text()
    linha4 = tela_cadastro.lineEdit.text()

    print("Nome do Produto:", linha1)
    print("Valor:", linha2)
    print("Código de Barras:", linha3)
    print("Descrição:", linha4)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (nome,preco,codigo,descricao) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), str(linha4))
    cursor.execute(comando_SQL, dados)
    banco.commit()


    tela_cadastro.lineEdit_2.setText("")
    tela_cadastro.lineEdit_3.setText("")
    tela_cadastro.lineEdit_4.setText("")
    tela_cadastro.lineEdit.setText("")


def deletar():
    linha = tela_estoque.lineEdit.text()

    cursor = banco.cursor()
    comando_SQL = "DELETE FROM produtos WHERE id = (%s)"
    dados = (str(linha))
    cursor.execute(comando_SQL, (dados,))
    banco.commit()

    print("Produto Deletado:", linha)

    tela_estoque.lineEdit.setText("")

def Caixa():
    tela_caixa.show()

    linha = tela_caixa.lineEdit.text()

    cursor = banco.cursor()
    comando_SQL = "SELECT Nome, EAN, Preço FROM produtos WHERE EAN = (%s)"
    dados = (str(linha))
    cursor.execute(comando_SQL, (dados,))
    dados = cursor.fetchall()
    

    print(dados)
    

    tela_caixa.tableWidget.setRowCount(len(dados))
    tela_caixa.tableWidget.setColumnCount(3)

    for i in range(0, len(dados)):
        for j in range(0, 3):
            tela_caixa.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))
            


app = QtWidgets.QApplication([])
menu = uic.loadUi("Menu.ui")
tela_caixa = uic.loadUi("Caixa.ui")
tela_cadastro = uic.loadUi("Cadastro_Produto.ui")
tela_estoque = uic.loadUi("Estoque.ui")
tela_deletarProduto = uic.loadUi("Deletar_Produto.ui")

tela_cadastro.pushButton.clicked.connect(cadastro)
tela_deletarProduto.pushButton.clicked.connect(deletar)
tela_caixa.pushButton.clicked.connect(Caixa)

menu.actionProduto.triggered.connect(chama_tela_cadastro)
menu.actionEstoque.triggered.connect(chama_tela_estoque)
menu.actionCaixa.triggered.connect(Caixa)


menu.show()
app.exec()