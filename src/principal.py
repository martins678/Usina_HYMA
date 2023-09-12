import sys

from instituicao.material import Material
from admin.material_control import MaterialControl

from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QLabel
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt


class Principal (Ui_MainWindow, QMainWindow): #Classe Principal:
#define uma classe chamada Principal, que é uma subclasse de duas classes: Ui_MainWindow e QMainWindow
    
    def __init__(self, parent = None) -> None: #Método __init__:
#na classe Principal __init__, é um metódo construtor da classe. Ele é chamado quando um objeto da classe é criado. (argumento opcional chamado parent, que é definido como None)
        super().__init__(parent) #Chama o construtor da classe usando a função super(), isso inicializa essas classes
        super().setupUi(self)#Chama o método setupUi() da classe para configurar a interface do usuário da janela principal (self refere-se à instância atual da classe Principal). 
        #Este método é geralmente gerado automaticamente a partir do Designer do PyQt e configura a interface do usuário com os elementos da GUI. 
        self._init_components()# Chama um método que é usado para inicializar os componentes adicionais da interface do usuário.
        self.controle_material = MaterialControl() #Cria uma instância da classe MaterialControl e a atribui ao atributo controle_material do objeto 
        self.cor_sucesso = 'background-color: rgb(66, 245, 170);'
        self.cor_erro = 'background-color: rgb(242, 70, 70);' #Define dois atributos de string cor_sucesso e cor_erro. 
        # Lista de usuários
        self.usuarios = {
            'fiscal': '123',
            'fiscal2': 'senha2',
            'fiscal3': 'senha3',
        }       

    def _init_components(self) -> None: # é responsável por inicializar e configurar alguns componentes da interface gráfica da classe.
        #tela_login apresentação da página inicial
        self.label_login_img.setPixmap(QPixmap('img/img_logo_maior'))#está definindo a imagem exibida em um objeto 
        self.frame_login_msg.hide()#está escondendo um componente da interface gráfica. Significa que inicialmente o componente estará oculto quando a interface for exibida.
        self.pushButton_login_fechar_msg.clicked.connect(lambda: self.frame_login_msg.hide())#o botão chamado está sendo configurado para executar uma ação quando for clicado. A ação que está sendo configurada é ocultar o componente
        self.pushButton_login_entrar.clicked.connect(self.realizar_login)#Semelhante à linha anterior!
        
        #tela_home leva o usuário a página com as opções: cadastro, lista, sair.
        self.label_home_logo.setPixmap(QPixmap('img/img_logo_maior'))#define a imagem da logo exibida 
        self.pushButton_home_sair.setIcon(QIcon('img/icon_sair.png')) #atribui um icone ao botão
        self.pushButton_home_cadastro.clicked.connect(self.acessar_cadastro)#conecta a ação de clique neste botão. Quando o botão for clicado, a função será chamada.
        self.pushButton_home_lista.clicked.connect(self.acessar_lista)#parecido com o anterior 
        self.pushButton_home_sair.clicked.connect(self.sair_sistema) #esta função é responsável por encerrar o programa ou à saída do sistema.
        
        #tela_cadastro funcionalidade dos botões
        self.label_cadastro_logo.setPixmap(QPixmap('img/img_logo_menor')) #define imagem 
        self.frame_cadastro_msg.hide()#esconde um objeto
        self.pushButton_cadastro_fechar_msg.clicked.connect(lambda: self.frame_cadastro_msg.hide())#Isso conecta clique a uma ação que oculta o frame_cadastro_msg. Fazendo com que o quadro de mensagem seja escondido.
        self.pushButton_cadastro_salvar.clicked.connect(self.salvar_dados) #quando clicado, salva os dados inseridos na interface do usuário.
        self.pushButton_cadastro_limpar.clicked.connect(self.novo_formulario)#quando clicado, limpa ou redefine o formulário de entrada.
        self.pushButton_cadastro_lista.clicked.connect(self.acessar_lista)#quando clicado, permite o acesso a lista de itens. 
        
        #tela_lista exibir a lista
        self.label_lista_logo.setPixmap(QPixmap('img/img_logo_menor')) #Define uma imagem para um rótulo (QLabel) chamado label_lista_logo na tela. A imagem é definida usando setPixmap.
        self.frame_lista_msg.hide() #Oculta um widget de quadro (QFrame) chamado frame_lista_msg. (apresntação=Esse quadro provavelmente contém alguma mensagem ou notificação que pode ser exibida ou ocultada quando necessário)
        self.pushButton_lista_fechar_msg.clicked.connect(lambda: self.frame_lista_msg.hide()) #Cria uma conexão entre o botão pushButton_lista_fechar_msg e uma função anônima (lambda). 
        self.pushButton_lista_excluir.clicked.connect(self.excluir_material) #Cria uma conexão entre o botão pushButton_lista_excluir e o método excluir_material. 
        self.pushButton_lista_alterar.clicked.connect(self.alterar_material) #Cria uma conexão entre o botão pushButton_lista_alterar e o método alterar_material. 
        self.pushButton_lista_novo.clicked.connect(self.novo_formulario) #Cria uma conexão entre o botão pushButton_lista_novo e o método novo_formulario.
        self.pushButton_lista_home.clicked.connect(self.acessar_home) #Cria uma conexão entre o botão pushButton_lista_home e o método acessar_home. 
        
    
    def realizar_login(self):
        login = self.lineEdit_login_usuario.text() #está sendo obtido o texto inserido em um widget de linha de entrada chamado lineEdit_login_usuario e armazenando-o na variável login.
        senha = self.lineEdit_login_senha.text() #está sendo obtido o texto inserido em um widget de linha de entrada chamado lineEdit_login_senha e armazenando-o na variável senha. 
        
        if login in self.usuarios and self.usuarios[login] == senha:
        #login == 'fiscal' and senha == '123': #está sendo verificado se o valor de login é igual a 'fiscal' e o valor de senha é igual a '123'. 
            self.lineEdit_login_usuario.clear() #limpa o texto no widget de linha de entrada lineEdit_login_usuario, removendo qualquer texto que tenha sido digitado.
            self.lineEdit_login_senha.clear() #limpa o texto no widget de linha de entrada lineEdit_login_senha.
            self.frame_login_msg.hide() #oculta um quadro de mensagens ou notificações, usado para exibir mensagens de erro ou sucesso.
            self.acessar_home() #chama o método acessar_home, que direciona o usuário para a tela inicial ou para a próxima parte do programa após o login bem-sucedido.
        else:
            self.label_login_msg.setText('Usuário ou senha incorretos') # configura o texto de um widget de rótulo chamado label_login_msg para exibir a mensagem 'Usuário ou senha incorretos'.
            self.frame_login_msg.show() #mostra o quadro de mensagens ou notificações, exibindo a mensagem de erro para informar ao usuário que o login falhou.
    

    def salvar_dados(self):
        material = Material()
        material.fornecedor = self.lineEdit_cadastro_fornecedor.text()
        material.materia_prima = self.comboBox_cadastro_materia_prima.currentText()
        material.quantidade = int(self.comboBox_cadastro_quantidade.currentText())
        self.limpar_campos()
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


    def alterar_material(self):
        indice = self.tableWidget_lista_dados.currentRow()
        if indice >= 0:
            self.indice_linha_selecionada = indice
            material = self.controle_material.lista_materiais[indice]
            self.lineEdit_cadastro_fornecedor.setText(material.fornecedor)
            self.acessar_cadastro()
            self.pushButton_cadastro_salvar.clicked.connect(self.salvar_dados)
    
    def novo_formulario(self) -> None:
        self.lineEdit_cadastro_fornecedor.clear()
        self.comboBox_cadastro_materia_prima.setCurrentIndex(0)
        self.comboBox_cadastro_quantidade.setCurrentIndex(0)
        self.frame_cadastro_msg.hide()
        self.acessar_cadastro() 
        self.pushButton_cadastro_salvar.clicked.connect(self.salvar_dados)
    
    def limpar_campos(self):
        self.lineEdit_cadastro_fornecedor.clear()
        self.comboBox_cadastro_materia_prima.setCurrentIndex(0)
        self.comboBox_cadastro_quantidade.setCurrentIndex(0)


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