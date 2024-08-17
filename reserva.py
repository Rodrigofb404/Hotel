from quarto import Quarto
from cliente import Cliente

class Reserva():
    def __init__(self) -> None:
        self.__data_entrada = None
        self.__data_saida = None
        self.__quarto = None
        self.__cliente = None
        self.__status = None
        self.__n_reserva = None

    @property
    def status(self):
        return self.__status

    def criar_reserva(self, data_entrada : str, data_saida : str, quarto: Quarto, cliente : Cliente, n_reserva: int) -> None:
        self.__data_entrada = data_entrada
        self.__data_saida = data_saida
        self.__quarto = quarto
        self.__cliente = cliente
        self.__status = "Reservado"
        self.__n_reserva = n_reserva

        