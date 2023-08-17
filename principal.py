import sys 

from model.UsinaBiodiesel import Usina_Biodiesel

from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPixmap
from principal import Ui_MainWindow

class Principal (Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.lista_biodiesel = []
        self.imagem_login.setPixmap(QPixmap('x.png'))
        self.frame_erro_login.hide()

        self.botao_ok_login.clicked.connect(lambda: self.frame_erro_login.hide())
        self.botao_entrar.clicked.connect(self.realizar_login)
        self.botao_cadastro.clicked.connect(self.cadastro)
        self.botao_sair.clicked.connect(self.sair)
        self.botao_salvar.clicked.connect(self.salvar_dados)

    def realizar_login(self):
        login = self.insira_login.text()
        senha = self.insira_senha.text()
        if login == 'fiscal' and senha == '123':
            print(self.insira_login.text())
            self.insira_login.setText('')
            self.insira_senha.setText('')
            self.frame_erro_login.hide()
            self.stackedWidget_paginas.setCurrentWidget(self.page_apresentacao)
        else:
            self.mensagem_erro.setText('Usuario ou senha incorreto')
            self.frame_erro_login.show()
    def cadastro(self):
        self.stackedWidget_paginas.setCurrentWidget(self.gui_cadastro)
        self.frame_4.hide()

    def sair(self):
        self.stackedWidget_paginas.setCurrentWidget(self.page_login)

    def salvar_dados(self):
        fornecedor = self.nome_fornecedor.text()
        materia_prima = self.nome_materia_prima.text()
        quantidade = self.quantidade_peso.text()
        print(f'Fornecedor: {fornecedor}\nMateria_prima: {materia_prima}\nQuantidade: {quantidade}')

        biodiesel = Usina_Biodiesel(fornecedor, materia_prima, int(quantidade))

        if biodiesel.error != '':
            self.mensage_erro2.setText(biodiesel.error)
            self.frame_4.show()
        else:
            self.lista_biodiesel.append(biodiesel)
            self.mensage_erro2.setText('Dados salvos com sucesso!')
            self.frame_4.show()
            self.nome_materia_prima.setFocus()

if __name__== '__main__':
    qt = QApplication(sys.argv)
    Principal = Principal()
    Principal.show()
    qt.exec()