class Cliente:
    def __init__(self, nome: str, idade: int, cpf: int, forma_pagamento: str, num_quarto : int) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__forma_pagamento = forma_pagamento
        self.num_quarto = num_quarto
    
    @property
    def nome(self):
        return self.__nome 
    
    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def forma_pagamento(self):
        return self.__forma_pagamento
    
# def main():
#     cliente = Cliente("Rodrigo", 20, 123456789)
#     print(cliente.nome)
#     print(cliente.idade)
#     print(cliente.cpf)
# main()
