'''CLASSES BASE E INTERFACES'''
from abc import ABC, abstractmethod

class Entidade(ABC):
    @abstractmethod
    def salvar(self):
        pass

    @abstractmethod
    def remover(self, id_entidade):
        pass
