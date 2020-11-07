from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTableView, QTableWidget, QPushButton, QMessageBox
from PyQt5 import uic
import mysql.connector


banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "teste"

)

lista = []

def chama_tela_cadastro():
    tela_cadastro.show()

def chama_tela_editar():
    tela_editarEstoque.show()

def chama_tela_caixa():
    tela_caixa.show()

def chama_tela_Orcamento_Cliente():
    tela_orcamento_cliente.show()


def chama_tela_Orcamento_Papelaria():
    tela_orcamento_papelaria.show()    


def chama_tela_caixa2():
    tela_compra.show()

def limpa_tabela():
    tela_caixa.tableWidget.clear()
    

def chama_tela_estoque():
    tela_estoque.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT *FROM  produtos"
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
    linha7 = tela_cadastro.lineEdit_Descricao.text()

    if linha1 == "" or linha2 == "" or linha3 == "" :
        QMessageBox.about(tela_cadastro, "Aviso","Campos Incorretos ou Vazios!")
    else:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO Produtos (Nome,EAN,Estoque,Preco,Altura,Largura,Descricao) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5), str(linha6),  str(linha7))
        cursor.execute(comando_SQL, dados)
        banco.commit()


        tela_cadastro.lineEdit_NomeProduto.setText("")
        tela_cadastro.lineEdit_Ean.setText("")
        tela_cadastro.lineEdit_Estoque.setText("")
        tela_cadastro.lineEdit_Preco.setText("")
        tela_cadastro.lineEdit_Altura.setText("")
        tela_cadastro.lineEdit_Largura.setText("")
        tela_cadastro.lineEdit_Descricao.setText("")

        QMessageBox.about(tela_cadastro, "Aviso","Produto Cadastrado!")
   

def cadastro_Orcamento_Cliente():
    linha1 = tela_orcamento_cliente.lineEdit_NomeProduto.text()
    linha2 = tela_orcamento_cliente.spinBox_uni.value()
    linha3 = tela_orcamento_cliente.spinBox_qtd.value()
    linha4 = tela_orcamento_cliente.lineEdit_unid.text()
    linha5 = tela_orcamento_cliente.lineEdit_total.text()
    linha6 = tela_orcamento_cliente.lineEdit_frete.text()
    linha7 = tela_orcamento_cliente.spinBox_desconto.value()
    linha8 = tela_orcamento_cliente.lineEdit_desc.text()

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO realizar_orcamento (Nome_Produto,Descrição_Produto,Unidade,Qtd,Desconto,Preco_uni,Preco_total,Frete) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1), str(linha8), str(linha2), str(linha3), str(linha7), str(linha4),  str(linha5), str(linha6))
    cursor.execute(comando_SQL, dados)
    banco.commit()

    tela_orcamento_cliente.lineEdit_NomeProduto.setText("")
    tela_orcamento_cliente.spinBox_uni.setValue(0)
    tela_orcamento_cliente.spinBox_qtd.setValue(0)
    tela_orcamento_cliente.lineEdit_unid.setText("")
    tela_orcamento_cliente.lineEdit_total.setText("")
    tela_orcamento_cliente.lineEdit_frete.setText("")
    tela_orcamento_cliente.spinBox_desconto.setValue(0)
    tela_orcamento_cliente.lineEdit_desc.setText("")

    QMessageBox.about(tela_orcamento_cliente, "Aviso","Produto Cadastrado!")

def Orcamento_Cliente():
    tela_orcamento_cliente.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT *FROM  realizar_orcamento"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()

    tela_orcamento_cliente.tableWidget_2.setRowCount(len(dados))
    tela_orcamento_cliente.tableWidget_2.setColumnCount(9)

    for i in range(0, len(dados)):
        for j in range(0, 9):
            tela_orcamento_cliente.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))

def pesquisar():
    try:    
        linha = tela_editarEstoque.lineEdit_Ean.text()
    
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM  produtos WHERE EAN = (%s)"
        dados = (str(linha))
        cursor.execute(comando_SQL, (dados,))
        dados1 = cursor.fetchall()
        

        tela_editarEstoque.lineEdit_NomeProduto.setText(dados1[0][1])
        tela_editarEstoque.lineEdit_Estoque.setText(dados1[0][3])
        tela_editarEstoque.lineEdit_Preco.setText(str(dados1[0][4]))
        tela_editarEstoque.lineEdit_Altura.setText(dados1[0][5])
        tela_editarEstoque.lineEdit_Largura.setText(dados1[0][6])
        tela_editarEstoque.lineEdit_Descricao.setText(dados1[0][7])
    except IndexError:
        QMessageBox.about(tela_editarEstoque, "Aviso","Produto Não encontrado!")

def editar():
    linha1 = tela_editarEstoque.lineEdit_NomeProduto.text()
    linha2 = tela_editarEstoque.lineEdit_Estoque.text()
    linha3 = tela_editarEstoque.lineEdit_Preco.text()
    linha4 = tela_editarEstoque.lineEdit_Altura.text()
    linha5 = tela_editarEstoque.lineEdit_Largura.text()
    linha6 = tela_editarEstoque.lineEdit_Descricao.text()
    linha7 = tela_editarEstoque.lineEdit_Ean.text()

    cursor = banco.cursor()
    comando_SQL = "UPDATE produtos SET Nome = (%s), Estoque = (%s), Preco = (%s), Altura = (%s), Largura = (%s), Descricao = (%s) WHERE EAN = (%s)"
    dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5), str(linha6),  str(linha7))
    cursor.executemany(comando_SQL, (dados,))
    banco.commit()

    tela_editarEstoque.lineEdit_NomeProduto.setText("")
    tela_editarEstoque.lineEdit_Ean.setText("")
    tela_editarEstoque.lineEdit_Estoque.setText("")
    tela_editarEstoque.lineEdit_Preco.setText("")
    tela_editarEstoque.lineEdit_Altura.setText("")
    tela_editarEstoque.lineEdit_Largura.setText("")
    tela_editarEstoque.lineEdit_Descricao.setText("")

    if cursor.executemany() == True:
        QMessageBox.about(tela_editarEstoque, "Aviso","Produto Editado!")
    else:
        QMessageBox.about(tela_editarEstoque, "Aviso","Campos vazios ou preenchidos incorretamente!")


def deletar():
    try: 
        linha = tela_editarEstoque.lineEdit_Ean.text()
        if linha != "":
            cursor = banco.cursor()
            comando_SQL = "DELETE FROM produtos WHERE EAN = (%s)"
            dados = (str(linha))
            cursor.execute(comando_SQL, (dados,))
            banco.commit()

            

            tela_editarEstoque.lineEdit_Ean.setText("")
            tela_editarEstoque.lineEdit_NomeProduto.setText("")
            tela_editarEstoque.lineEdit_Estoque.setText("")
            tela_editarEstoque.lineEdit_Preco.setText("")
            tela_editarEstoque.lineEdit_Altura.setText("")
            tela_editarEstoque.lineEdit_Largura.setText("")
            tela_editarEstoque.lineEdit_Descricao.setText("")
            QMessageBox.about(tela_editarEstoque, "Aviso","Produto Apagado!")
        
        else:
            QMessageBox.about(tela_editarEstoque, "Aviso","Revise os campos!")

    except Exception:    
            QMessageBox.about(tela_editarEstoque, "Aviso","Ocorreu um erro, revise os campos e tente novamente!")



def Caixa():
    quantidade = 0
    tela_caixa.comboBox.clear()
    
    try:
        linha = tela_caixa.lineEdit.text()
        cursor = banco.cursor()
        comando_SQL = "SELECT Nome, Estoque, Preco, EAN FROM  produtos WHERE EAN = (%s)"
        dados = (str(linha))
        cursor.execute(comando_SQL, (dados,))
        dados1 = cursor.fetchall()
        quantidade = (dados1[0][1])
        quantidade1 = int(quantidade)
        
        
        for i in range (0, quantidade1+1):
            tela_caixa.comboBox.addItem(str(i))

        
    
    except IndexError:
        QMessageBox.about(tela_editarEstoque, "Aviso","Produto Não encontrado!")      
       
def Caixa_Adicionar():
    soma = []
    total = 0
    lista_final = []
    linha = tela_caixa.lineEdit.text()
    cursor = banco.cursor()
    comando_SQL = "SELECT Nome, Estoque, Preco, EAN FROM  produtos WHERE EAN = (%s)"
    dados = (str(linha))
    cursor.execute(comando_SQL, (dados,))
    dados1 = cursor.fetchall()

    lista.append([dados1[0][0],tela_caixa.comboBox.currentText(),dados1[0][2],dados1[0][3]])
    
    tela_caixa.pushButton_Limpar.clicked.connect(limpa_tabela)
    tela_caixa.tableWidget.setRowCount(len(lista))
    tela_caixa.tableWidget.setColumnCount(4)

    for list in lista:
        soma.append((list[2])*float(list[1]))
        total = sum(soma)
        tela_caixa.label_valor.setText(str(float("%.3f" % total)))
        #lista_final.append(lista[0],lista[3],)   
        print(lista_final)
        for i in range(0, len(lista)):
            for j in range(0, 4):
                    tela_caixa.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(lista[i][j])))
                    
    
    

    

    #cursor = banco.cursor()
    #comando_SQL = "UPDATE produtos SET Estoque = Estoque - (%s); WHERE EAN = (%s)"
    #dados1 = (str(list[1]))
    #dados2 = (str(dados1[0][3]))
    #cursor.execute(comando_SQL, dados1, (dados2,))


    #if tela_compra.radioButton_1.isChecked() == True:
        #tela_compra.lineEdit.setEnabled(True)
        #tela_compra.label_4.setEnabled(True)
        #tela_compra.label_5.setEnabled(True)
    #else:
        #tela_compra.lineEdit.setEnabled(False)
        #tela_compra.label_4.setEnabled(False)
        #tela_compra.label_5.setEnabled(False)
    






app = QtWidgets.QApplication([])
menu = uic.loadUi("Menu.ui")
tela_caixa = uic.loadUi("Caixa.ui")
tela_cadastro = uic.loadUi("Cadastro_Produto.ui")
tela_estoque = uic.loadUi("Estoque.ui")
tela_orcamento_cliente = uic.loadUi("Realizar_Orcamento_Cliente_Empresa.ui")
#tela_orcamento_papelaria = uic.loadUi("Orcamento_Papelaria.ui")
tela_editarEstoque = uic.loadUi("Estoque_Editar.ui")
tela_compra = uic.loadUi("Caixa_Final.ui")

tela_cadastro.pushButton.clicked.connect(cadastro)
tela_editarEstoque.pushButton_deletar.clicked.connect(deletar)
tela_caixa.pushButton_pesquisa.clicked.connect(Caixa)
tela_caixa.pushButton.clicked.connect(Caixa_Adicionar)
tela_editarEstoque.pushButton_pesquisar.clicked.connect(pesquisar)
tela_editarEstoque.pushButton_editar.clicked.connect(editar)
tela_estoque.pushButton.clicked.connect(chama_tela_estoque)
tela_caixa.pushButton_2.clicked.connect(chama_tela_caixa2)
tela_orcamento_cliente.pushButton_criar.clicked.connect(cadastro_Orcamento_Cliente)
tela_orcamento_cliente.pushButton_atualizar.clicked.connect(Orcamento_Cliente)


menu.actionProduto.triggered.connect(chama_tela_cadastro)
menu.actionEstoque.triggered.connect(chama_tela_estoque)
menu.actionCaixa.triggered.connect(chama_tela_caixa)
menu.actionEditar_Estoque.triggered.connect(chama_tela_editar)
#menu.actionOr_amento_Papelaria.triggered.connect(chama_tela_Orcamento_Papelaria)
menu.actionOr_amento_Cliente_Empresa.triggered.connect(chama_tela_Orcamento_Cliente)

menu.show()
app.exec()