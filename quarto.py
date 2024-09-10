class Quarto():
    def __init__(self, numero: int, tipo_quarto: int, preco: int) -> None: # tipo_quarto 1: Suíte Presidencial 2: Suíte com varanda | 3: Suíte | 4: quarto simples 
        self.__numero = numero
        self.__tipo_quarto = tipo_quarto
        self.__preco = preco
        self.disponibilidade = True

    @property
    def numero(self):
        return self.__numero
    
    @property
    def tipo_quarto(self):
        return self.__tipo_quarto
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        if (novo_preco > self.preco):
            self.__preco = novo_preco
        else:
            print("Insira um valor válido!")

    