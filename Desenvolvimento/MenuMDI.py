from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTableWidget, QPushButton
import sys
from PyQt5 import uic
import mysql.connector

app = QApplication(sys.argv)



banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "teste"

)


menu = uic.loadUi("Menu.ui")
tela_cadastro = uic.loadUi("Cadastro_Produto.ui")
tela_deletarProduto = uic.loadUi("Deletar_Produto.ui")
tela_estoque = uic.loadUi("Estoque.ui")
tela_estoque_editar = uic.loadUi("Estoque_Editar.ui")

class MDIWindow(QMainWindow):
    
    
    count = 0
    def __init__(self):
        super().__init__()
 
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        bar.setStyleSheet("color: black;"
                        "background-color: #00BFFF;"
                        "selection-color: black;"
                        "selection-background-color: #DAA520;");


        file = bar.addMenu("Produtos")
        file.addAction("Cadastrar Produto")
        file.addAction("Deletar Produto")
        file.addAction("Estoque")
        file.addAction("Editar Estoque")
        file.triggered[QAction].connect(self.CriacaoTela)
        self.setWindowTitle("Papelaria ABC")
 
    def CriacaoTela(self, p):
        
        if p.text() == "Cadastrar Produto":
            MDIWindow.count = MDIWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWindowTitle("Cadastrar Produto")
            sub.setGeometry(0,0,600,600)
            self.mdi.addSubWindow(sub)
            sub.setWidget(tela_cadastro)
            sub.show()
            
                
        
            

        if p.text() == "Deletar Produto":
            sub = QMdiSubWindow()
            sub.setWidget(tela_deletarProduto)
            sub.setWindowTitle("Deletar Produto")
            sub.setGeometry(0,0,600,600)
            self.mdi.addSubWindow(sub)
            deletar()
            sub.show()   
            
        if p.text() == "Estoque":
            sub = QMdiSubWindow()
            sub.setWidget(tela_estoque)
            sub.setWindowTitle("Estoque")
            sub.setGeometry(0,0,600,600)
            self.mdi.addSubWindow(sub)
            chama_tela_estoque()
            sub.show()    

    
        if p.text() == "Editar Estoque":
            sub = QMdiSubWindow()
            sub.setWidget(tela_estoque_editar)
            sub.setWindowTitle("Editar Estoque")
            sub.setGeometry(0,0,600,600)
            self.mdi.addSubWindow(sub)
            sub.show()
 




def chama_tela_estoque():
    tela_estoque.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT *FROM  Produtos"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()
    

    tela_estoque.tableWidget.setRowCount(len(dados))
    tela_estoque.tableWidget.setColumnCount(8)


    for i in range(0, len(dados)):
        for j in range(0, 8):
            tela_estoque.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))

def cadastro():
    
    linha1 = tela_cadastro.lineEdit_NomeProduto.text()
    linha2 = tela_cadastro.lineEdit_Ean.text()
    linha3 = tela_cadastro.lineEdit_Estoque.text()
    linha4 = tela_cadastro.lineEdit_Preco.text()
    linha5 = tela_cadastro.lineEdit_Altura.text()
    linha6 = tela_cadastro.lineEdit_Largura.text()
    linha8 = tela_cadastro.lineEdit_Descricao.text()


    cursor = banco.cursor()
    comando_SQL = "INSERT INTO Produtos (Nome,EAN,Estoque,Preço,Altura,Largura,Descrição) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5), str(linha6),  str(linha8))
    cursor.execute(comando_SQL, dados)
    banco.commit()


    tela_cadastro.lineEdit_NomeProduto.setText("")
    tela_cadastro.lineEdit_Ean.setText("")
    tela_cadastro.lineEdit_Estoque.setText("")
    tela_cadastro.lineEdit_Preco.setText("")
    tela_cadastro.lineEdit_Altura.setText("")
    tela_cadastro.lineEdit_Largura.setText("")
    tela_cadastro.lineEdit_Descricao.setText("")



def deletar():
    
    tela_deletarProduto.show()

    linha = tela_deletarProduto.lineEdit.text()  

    cursor = banco.cursor()
    comando_SQL = "DELETE FROM Produtos WHERE id = (%s)"
    dados = (str(linha))
    cursor.execute(comando_SQL, (dados,))

    comando_SQL2 = "SELECT *FROM  Produtos"
    cursor.execute(comando_SQL2)
    dados2 = cursor.fetchall()
    

    tela_deletarProduto.tableWidget.setRowCount(len(dados2))
    tela_deletarProduto.tableWidget.setColumnCount(8)

    for i in range(0, len(dados2)):
        btn_editar = QPushButton("Editar")
        btn_editar.clicked.connect()
        tela_deletarProduto.tableWidget.setItem(btn_editar)
        for j in range(0, 8):
            tela_deletarProduto.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados2[i][j])))

    banco.commit()

    tela_deletarProduto.lineEdit.setText("")
    tela_deletarProduto.show()
    
def EditarEstoque ():
    cursor = banco.cursor()
    comando_SQL = "SELECT *FROM  Produtos"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()
    lista =[]
    lista.append(dados)
    tela_estoque_editar.comboBox.addItems(lista)


          


 
tela_cadastro.pushButton.clicked.connect(cadastro)
tela_deletarProduto.pushButton.clicked.connect(deletar)

mdi = MDIWindow()
mdi.show()
app.exec_()