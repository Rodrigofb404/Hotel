# from cliente import Cliente
from quarto import Quarto
from reserva import Reserva

class Hotel:
    def __init__(self, reserva: Reserva, quartos: Quarto) -> None:
        self.qtd_quartos = 0
        self.quartos_livres = 0
        self.reservas = []
        self.quartos = []

    