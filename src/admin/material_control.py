from typing import List
from instituicao.material import Material

class MaterialControl:

    def __init__(self) -> None:
        self.lista_materiais:List[Material] = []
    
    def add_material(self, material):
        if isinstance(material, Material):
            self.lista_materiais.append(material)
        return 'Material salvo com sucesso'
    
    def excluir_material(self, indice:int):
        del self.lista_materiais[indice]
        return 'Material excluído com sucesso'

    @property
    def lista_materiais(self) -> List[Material]:
        return self.__lista_materiais
    
    @lista_materiais.setter
    def lista_materiais(self, lista) -> None:
        self.__lista_materiais:List[Material] = []