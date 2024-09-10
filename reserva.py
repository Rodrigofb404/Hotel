from quarto import Quarto
from cliente import Cliente

class Reserva():
    def __init__(self, data_entrada : str, data_saida : str, quarto: Quarto, cliente : Cliente, n_reserva : int) -> None:
        self.__data_entrada = data_entrada
        self.__data_saida = data_saida
        self.__quarto = quarto
        self.__cliente = cliente
        self.__n_reserva = n_reserva
        

    @property
    def data_entrada(self):
        return self.__data_entrada

    @property
    def data_saida(self):
        return self.__data_saida

    @property
    def quarto(self):
        return self.__quarto
        
    @property
    def cliente(self):
        return self.__cliente

    @property
    def n_reserva(self):
        return self.__n_reserva

    @n_reserva.setter
    def set_n_reserva(self, n_reserva):
        self.__n_reserva = n_reserva

    # def criar_reserva(self, data_entrada : str, data_saida : str, quarto: Quarto, cliente : Cliente, n_reserva: int) -> None:
    #     self.__data_entrada = data_entrada
    #     self.__data_saida = data_saida
    #     self.__quarto = quarto
    #     self.__cliente = cliente
    #     self.__status = "Reservado"
    #     self.__n_reserva = n_reserva

        