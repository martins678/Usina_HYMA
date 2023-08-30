import sys

from instituicao.material import Material
from admin.material_control import MaterialControl

from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QLabel
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt


class Principal (Ui_MainWindow, QMainWindow):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self._init_components()
        self.controle_material = MaterialControl()
        self.cor_sucesso = 'background-color: rgb(66, 245, 170);'
        self.cor_erro = 'background-color: rgb(242, 70, 70);'

    def _init_components(self) -> None:
        #tela_login apresentação da página inicial
        self.label_login_img.setPixmap(QPixmap('img/img_logo_maior'))
        self.frame_login_msg.hide()
        self.pushButton_login_fechar_msg.clicked.connect(lambda: self.frame_login_msg.hide())
        self.pushButton_login_entrar.clicked.connect(self.realizar_login)

        #tela_home leva o usuário a página com as opções: cadastro, lista, sair.
        self.label_home_logo.setPixmap(QPixmap('img/img_logo_maior'))
        self.pushButton_home_sair.setIcon(QIcon('img/icon_sair.png'))
        self.pushButton_home_cadastro.clicked.connect(self.acessar_cadastro)
        self.pushButton_home_lista.clicked.connect(self.acessar_lista)
        self.pushButton_home_sair.clicked.connect(self.sair_sistema)

        #tela_cadastro funcionalidade dos botões
        self.label_cadastro_logo.setPixmap(QPixmap('img/img_logo_menor'))
        self.frame_cadastro_msg.hide()
        self.pushButton_cadastro_fechar_msg.clicked.connect(lambda: self.frame_cadastro_msg.hide())
        self.pushButton_cadastro_salvar.clicked.connect(self.salvar_dados)
        self.pushButton_cadastro_limpar.clicked.connect(self.novo_formulario)
        self.pushButton_cadastro_lista.clicked.connect(self.acessar_lista)

        #tela_lista exibir a lista
        self.label_lista_logo.setPixmap(QPixmap('img/img_logo_menor'))
        self.frame_lista_msg.hide()
        self.pushButton_lista_fechar_msg.clicked.connect(lambda: self.frame_lista_msg.hide())
        self.pushButton_lista_excluir.clicked.connect(self.excluir_material)
        #self.pushButton_lista_alterar()
        self.pushButton_lista_novo.clicked.connect(self.novo_formulario)
        self.pushButton_lista_home.clicked.connect(self.acessar_home)
        
    def realizar_login(self):
        login = self.lineEdit_login_usuario.text()
        senha = self.lineEdit_login_senha.text()
        if login == 'fiscal' and senha == '123':
            self.lineEdit_login_usuario.clear()
            self.lineEdit_login_senha.clear()
            self.frame_login_msg.hide()
            self.acessar_home()
        else:
            self.label_login_msg.setText('Usuário ou senha incorretos')
            self.frame_login_msg.show()

    def salvar_dados(self):
        material = Material()
        material.fornecedor = self.lineEdit_cadastro_fornecedor.text()
        material.materia_prima = self.comboBox_cadastro_materia_prima.currentText()
        material.quantidade = int(self.comboBox_cadastro_quantidade.currentText())
        if material.error != '':
            self.label_cadastro_msg.setText(material.error)
            self.label_cadastro_msg.setStyleSheet(self.cor_erro)
            self.frame_cadastro_msg.show()
        else:
            msg = self.controle_material.add_material(material)
            self.label_cadastro_msg.setText(msg)
            self.label_cadastro_msg.setStyleSheet(self.cor_sucesso)
            self.frame_cadastro_msg.show()
            self.listar_material_tabela()
    
    def listar_material_tabela(self):
        cont_linhas = 0
        self.tableWidget_lista_dados.clearContents()
        self.tableWidget_lista_dados.setRowCount(len(self.controle_material.lista_materiais))
        for material in self.controle_material.lista_materiais:
            self.tableWidget_lista_dados.setItem(cont_linhas, 1, QTableWidgetItem(material.fornecedor))
            self.tableWidget_lista_dados.setItem(cont_linhas, 2, QTableWidgetItem(material.materia_prima))
            self.tableWidget_lista_dados.setItem(cont_linhas, 3, QTableWidgetItem(str(material.quantidade)))
            self.tableWidget_lista_dados.setItem(cont_linhas, 4, QTableWidgetItem(material.dia_da_semana))
            cont_linhas += 1
    
    def excluir_material(self) -> None:
        indice = self.tableWidget_lista_dados.currentRow()
        if indice >= 0:
            msg = self.controle_material.excluir_material(indice)
            self.tableWidget_lista_dados.removeRow(indice)
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_sucesso)
            self.frame_lista_msg.show()
        else:
            msg = 'Selecione a linha referente ao material que deseja excluir'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()

    def novo_formulario(self) -> None:
        self.lineEdit_cadastro_fornecedor.clear()
        self.comboBox_cadastro_materia_prima.setCurrentIndex(0)
        self.comboBox_cadastro_quantidade.setCurrentIndex(0)
        self.frame_cadastro_msg.hide()
        self.acessar_cadastro()

    # Métodos Gerais

    def acessar_home(self) -> None:
        
        #Acessa a página Home
        
        self.stackedWidget_paginas.setCurrentWidget(self.page_home)

    def acessar_cadastro(self) -> None:
        
        #Acessa a página Cadastro
    
        self.stackedWidget_paginas.setCurrentWidget(self.page_cadastro)

    def acessar_lista(self) -> None:
        
        #Acessa a página Lista
        
        self.stackedWidget_paginas.setCurrentWidget(self.page_lista)

    def sair_sistema(self) -> None:
        

        #Faz Logoff
        
        self.stackedWidget_paginas.setCurrentWidget(self.page_login)


if __name__== '__main__':
    qt = QApplication(sys.argv)
    Principal = Principal()
    Principal.show()
    qt.exec()