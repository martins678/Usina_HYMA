from datetime import date 

class Material:

    def __init__(self, fornecedor = None, materia_prima = None, quantidade:int = None):
        self.error = ''
        self.fornecedor = fornecedor
        self.materia_prima = materia_prima
        self.quantidade = quantidade
        self.__DIAS = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
        self.dia_da_semana = ''
        
    @property
    def dia_da_semana(self):
        return self.__dia_da_semana 
    
    @dia_da_semana.setter 
    def dia_da_semana(self, dia):
        self.__dia_da_semana = self.__DIAS [date.today().weekday()]

    @property
    def fornecedor(self):
        return self.__fornecedor 
    
    @fornecedor.setter 
    def fornecedor(self, fornecedor):
        if fornecedor != None and len(fornecedor) != 0:
            self.__fornecedor = fornecedor
        else: 
            self.error = "O campo 'Fornecedor' é obrigatório!"

    @property
    def materia_prima(self):
        return self.__materia_prima
    
    @materia_prima.setter
    def materia_prima(self, materia_prima):
        if materia_prima != '---': 
            self.__materia_prima = materia_prima
        else: 
            self.error = "O campo 'Matéria-Prima' não pode ser vazio."

    @property
    def quantidade(self): 
        return self.__quantidade
    
    @quantidade.setter 
    def quantidade(self, quantidade:int): #""
        if quantidade != 0:
            self.__quantidade = quantidade
        else: 
            self.error = "O campo 'Quantidade' não pode ser zero (0)."
        
    def __str__(self):
        return f" fornecedor: {self.fornecedor} \
| materia_prima: {self.materia_prima} \
| quantidade: {self.quantidade} \
| dias_da_semana: {self.dia_da_semana}"
        
mat = Material('Gomes', 'coco', 5)
print(mat)