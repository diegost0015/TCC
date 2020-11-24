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
lista2 = []

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




def limpa_tabela():
    tela_caixa.tableWidget.clear()

def limpa_lista():
    lista.clear()
    

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
    comando_SQL = "INSERT INTO realizar_orcamento (Nome_Produto,Frete,Unidade,Qtd,Desconto,Preco_uni,Preco_total,Descrição_Produto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1), str(linha6), str(linha2), str(linha3), str(linha7), str(linha4),  str(linha5), str(linha8))
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

    QMessageBox.about(tela_orcamento_cliente, "Aviso","Orçamento Criado!")

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
    global total2 
    soma2 = []
    linha = tela_caixa.lineEdit.text()
    cursor = banco.cursor()
    comando_SQL = "SELECT Nome, Estoque, Preco, EAN FROM  produtos WHERE EAN = (%s)"
    dados = (str(linha))
    cursor.execute(comando_SQL, (dados,))
    dados1 = cursor.fetchall()
    
    lista.append([dados1[0][0],tela_caixa.comboBox.currentText(),dados1[0][2],dados1[0][3]])


    data_compra = tela_caixa.calendarWidget.selectedDate()

    tela_caixa.pushButton_Limpar.clicked.connect(limpa_tabela)
    tela_caixa.tableWidget.setRowCount(len(lista))
    tela_caixa.tableWidget.setColumnCount(4)

    for list in lista:
        soma2.append((list[2])*float(list[1]))
        total2 = sum(soma2)
        tela_caixa.label_valor.setText(str(float("%.3f" % total2)))  
        for i in range(0, len(lista)):
            for j in range(0, 4):
                    tela_caixa.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(lista[i][j])))
                    
    
    

    
def finalizar_compra():
    
    total = 0 
    frm_pagamento = ""
    data_compra = ""
    soma = []
    lista_final = []
    linha = tela_caixa.lineEdit.text()
    cursor = banco.cursor()

    comando_SQL = "SELECT Nome, Estoque, Preco, EAN FROM  produtos WHERE EAN = (%s)"
    dados = (str(linha))
    cursor.execute(comando_SQL, (dados,))
    dados1 = cursor.fetchall()

    

    if tela_caixa.radioButton_1.isChecked() == True:
        frm_pagamento = tela_caixa.radioButton_1.text()  


    elif tela_caixa.radioButton_2.isChecked() == True:
        frm_pagamento = tela_caixa.radioButton_2.text()

    elif tela_caixa.radioButton_3.isChecked() == True:
        frm_pagamento = tela_caixa.radioButton_3.text()


    data_compra = tela_caixa.calendarWidget.selectedDate()
    print (data_compra)
   
    for list in lista:
        soma.append((list[2])*float(list[1]))
        total = sum(soma)
        tela_caixa.label_valor.setText(str(float("%.3f" % total)))
        lista_final.append([list[0],list[3],list[2],list[1],frm_pagamento,data_compra])   
        print(lista_final)


    for list in lista_final:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO compra (nome, ean, preco, qtd, forma_pg, data_compra) VALUES (%s,%s,%s,%s,%s,%s)"
        dados = (str(list[0]), str(list[1]), str(list[2]), str(list[3]), str(list[4]), str(list[5]))
        cursor.execute(comando_SQL, dados)
        banco.commit()
    QMessageBox.about(tela_caixa, "Aviso","Compra Finalizada")
    limpa_lista()
    limpa_tabela()
    


def troco():
    try:
        resultado = 0
        troco = tela_caixa.lineEdit_2.text()
        print(total2)
        resultado =  float(troco) - total2
        tela_caixa.label_10.setText(str(float("%.3f" % resultado)))
    except NameError:
        QMessageBox.about(tela_caixa, "Aviso","Valor de compra não encontrado!")     
    
def relatorio_compras():   
    tela_RCompras.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT *FROM  compra"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()

    tela_RCompras.tableWidget.setRowCount(len(dados))
    tela_RCompras.tableWidget.setColumnCount(7)

    for i in range(0, len(dados)):
        for j in range(0, 7):
            tela_RCompras.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))


def deletar_compras():
    try: 
        linha = tela_RCompras.lineEdit.text()
        if linha != "":
            cursor = banco.cursor()
            comando_SQL = "DELETE  FROM compra WHERE id = (%s)"
            dados = (str(linha))
            cursor.execute(comando_SQL, (dados,))
            banco.commit()

            QMessageBox.about(tela_RCompras, "Aviso","Registro Apagado!")
        
        else:
            QMessageBox.about(tela_RCompras, "Aviso","Revise os campos!")

    except Exception:    
            QMessageBox.about(tela_RCompras, "Aviso","Ocorreu um erro, revise os campos e tente novamente!")  






app = QtWidgets.QApplication([])
menu = uic.loadUi("Menu.ui")
tela_caixa = uic.loadUi("Caixa.ui")
tela_cadastro = uic.loadUi("Cadastro_Produto.ui")
tela_estoque = uic.loadUi("Estoque.ui")
tela_orcamento_cliente = uic.loadUi("Realizar_Orcamento_Cliente_Empresa.ui")
#tela_orcamento_papelaria = uic.loadUi("Orcamento_Papelaria.ui")
tela_editarEstoque = uic.loadUi("Estoque_Editar.ui")
tela_RCompras = uic.loadUi("Relatorio_Compras.ui")


tela_cadastro.pushButton.clicked.connect(cadastro)
tela_editarEstoque.pushButton_deletar.clicked.connect(deletar)
tela_caixa.pushButton_pesquisa.clicked.connect(Caixa)
tela_caixa.pushButton.clicked.connect(Caixa_Adicionar)
tela_caixa.pushButton_Limpar.clicked.connect(limpa_tabela)
tela_caixa.pushButton_Limpar.clicked.connect(limpa_lista)
tela_editarEstoque.pushButton_pesquisar.clicked.connect(pesquisar)
tela_editarEstoque.pushButton_editar.clicked.connect(editar)
tela_estoque.pushButton.clicked.connect(chama_tela_estoque)
tela_caixa.pushButton_2.clicked.connect(finalizar_compra)
tela_caixa.pushButton_calc.clicked.connect(troco)
tela_RCompras.pushButton_2.clicked.connect(deletar_compras)
tela_RCompras.pushButton_atualizar.clicked.connect(relatorio_compras)

tela_orcamento_cliente.pushButton_criar.clicked.connect(cadastro_Orcamento_Cliente)
tela_orcamento_cliente.pushButton_atualizar.clicked.connect(Orcamento_Cliente)


menu.actionProduto.triggered.connect(chama_tela_cadastro)
menu.actionEstoque.triggered.connect(chama_tela_estoque)
menu.actionCaixa.triggered.connect(chama_tela_caixa)
menu.actionEditar_Estoque.triggered.connect(chama_tela_editar)
#menu.actionOr_amento_Papelaria.triggered.connect(chama_tela_Orcamento_Papelaria)
menu.actionOr_amento_Cliente_Empresa.triggered.connect(chama_tela_Orcamento_Cliente)
menu.actionRelat_rio_Compras.triggered.connect(relatorio_compras)

menu.show()
app.exec()