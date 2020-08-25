import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow

class Janela(QMainWindow):
    def __init__(self):
        #super para chamar a classe construtora da classe
        super().__init__(self)

        #abaixo as definições da janela...a altura e distancia na tela
        self.topo = 100 #lugar no topo da tela
        self.esquerda = 100 #distancia lateral
        self.largura = 800
        self.altura = 600
        self.titulo = "Janela - 1"
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show

#guia da aplicação
aplicacao = QApplication(sys.argv) #parâmetros para mexer no nosso sistema...fechar janela por exemplo.
#instanciando nossa janela
j = Janela()
sys.exit(aplicacao.exec_())
