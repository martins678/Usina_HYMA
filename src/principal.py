import sys

from model.UsinaBiodiesel import Usina_Biodiesel

from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class Principal (Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.lista_biodiesel = []
        self.stackedWidget_paginas.setCurrentWidget(self.page_login)
        self.frame_erro_login.hide()
        self.botao_ok_login.clicked.connect(lambda: self.frame_erro_login.hide())
        self.botao_entrar.clicked.connect(self.realizar_login)
        self.botao_cadastro.clicked.connect(self.cadastro)
        self.botao_sair.clicked.connect(self.sair)
        self.botao_salvar.clicked.connect(self.salvar_dados)
        self.botao_sair.setIcon(QIcon('imagem/icon_on_off.png'))
        self.botao_lista.clicked.connect(self.lista)

        self.set_label_imagem(self.imagem_login, 'imagem/imagem_logo.png')
        self.set_label_imagem(self.imagem_cadastro_2,'imagem/imagem_logo.png')
        

    def set_label_imagem(self, label: QLabel, end_imagem: str):
        imagem = QPixmap(end_imagem)
        imagem = imagem.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(imagem)
        

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
        materia_prima = self.nome_materia_prima.currentText()
        quantidade = self.nome_quantidade.currentText()
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
            self.stackedWidget_paginas.setCurrentWidget(self.page_lista)
    
    
    def lista (self):
        self.stackedWidget_paginas.setCurrentWidget(self.page_lista)


if __name__== '__main__':
    qt = QApplication(sys.argv)
    Principal = Principal()
    Principal.show()
    qt.exec()