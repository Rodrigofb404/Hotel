class Quarto:
    def __init__(self, numero: int, tipo: str, preco: int) -> None:
        self.__numero = numero
        self.__tipo = tipo
        self.__preco = preco
        self.disponibilidade = True

    @property
    def numero(self):
        return self.__numero
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        if (novo_preco > self.preco):
            self.__preco = novo_preco
        else:
            print("Insira um valor válido!")

    