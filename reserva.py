from quarto import Quarto
from cliente import 

class Reserva:
    def __init__(self, data_entrada : str, data_saida : str, quarto: Quarto, cliente : Cliente, status: str) -> None:
        self.__data_entrada = data_entrada
        self.__data_saida = data_saida
        self.__quarto = quarto
        self.__cliente = cliente
        self.__status = "Reservado"

    @property
    def status(self):
        return self.__status
    
    def cancelar_reserva(self):
        self.__status = "Cancelada"
        self.__quarto.disponibilidade = True
        print("Reserva cancelada")

    def finalizar_reserva(self):
        self.__status = "Finalizada"
        print("Reserva finalizada")

     