from PyQt5 import uic, QtWidgets


def chama_tela_cadastro():
    tela_cadastro.show()

def cadastro():
    linha1 = tela_cadastro.lineEdit_2.text()
    linha2 = tela_cadastro.lineEdit_3.text()
    linha3 = tela_cadastro.lineEdit_4.text()
    linha4 = tela_cadastro.lineEdit.text()

    print("Nome do Produto:", linha1)
    print("Valor:", linha2)
    print("Código de Barras:", linha3)
    print("Descrição:", linha4)


app = QtWidgets.QApplication([])
menu = uic.loadUi("Menu.ui")
tela_cadastro = uic.loadUi("Cadastro_Produto.ui")
tela_cadastro.pushButton.clicked.connect(cadastro)
menu.actionCadastro.triggered.connect(chama_tela_cadastro )

menu.show()
app.exec()