from random import randint
from cliente import Cliente
from quarto import Quarto
from reserva import Reserva

class Hotel:
    def __init__(self) -> None:
        self.qtd_quartos = 0
        self.quartos_livres = 0
        self.reservas_andamento = []
        self.reservas_finalizadas = []
        self.quartos = []

    def add_quarto(self, quarto : Quarto):
        self.quartos_livres += 1
        self.quartos.append(quarto)
        
    def gerar_n_reserva(self):
        flag = None
        n_reserva = randint(0, 1000)
        while(flag != 0): # Verifica se o número de reserva já existe
            flag = 0
            
            for reservas_and in self.reservas_andamento:
                if (n_reserva == reservas_and.n_reserva):
                    n_reserva = randint(0, 1000)
                    flag += 1
                    break
                
            for reservas_fin in self.reservas_finalizadas:
                if (n_reserva == reservas_fin.n_reserva):
                    n_reserva = randint(0, 1000)
                    flag += 1
                    break
        
        return n_reserva
       
    def verificar_disponibilidade_quarto(self, quarto : Quarto):
        for room in self.quartos:
            if(quarto.numero == room.numero and room.disponibilidade):
                return True

        print("Quarto indisponível!")
        return False
                     
    def criar_reserva(self, data_entrada : str, data_saida : str, quarto: Quarto, cliente : Cliente):
        n_reserva = self.gerar_n_reserva()
        
        if (self.verificar_disponibilidade_quarto(quarto)):
            self.reservas_andamento.append(Reserva(data_entrada, data_saida, quarto, cliente, n_reserva))
            quarto.disponibilidade = False
            self.quartos_livres -= 1
            print(f"Reserva nº {n_reserva} criada com sucesso!")
            return
            
    def finalizar_reserva(self, n_reserva : Reserva.n_reserva):
        for res in self.reservas_andamento:
            if (n_reserva == res.n_reserva):
                self.reservas_finalizadas.append(res)
                res.quarto.disponibilidade = True
                self.reservas_andamento.remove(res)
                return

    def pesquisar_reserva(self, n_reserva):
        for reserva_and in self.reservas_andamento:
            if (n_reserva == reserva_and.n_reserva):
                print(f"------------ RESERVA Nº {n_reserva} ------------")
                print(f"Cliente: {reserva_and.cliente.nome} | CPF: {reserva_and.cliente.cpf}")        
                print(f"Quarto Nº {reserva_and.quarto.numero} | Tipo: {reserva_and.quarto.tipo_quarto}")        
                print(f"Período da reserva_and: {reserva_and.data_entrada} - {reserva_and.data_saida}")
                print(f"Status da reserva: ANDAMENTO")
                return     

        for reserva_fin in self.reservas_finalizadas:
            if (n_reserva == reserva_fin.n_reserva):
                print(f"------------ RESERVA Nº {n_reserva} ------------")
                print(f"Cliente: {reserva_fin.cliente.nome} | CPF: {reserva_fin.cliente.cpf}")        
                print(f"Quarto Nº {reserva_fin.quarto.numero} | Tipo: {reserva_fin.quarto.tipo_quarto}")        
                print(f"Período da reserva_fin: {reserva_fin.data_entrada} - {reserva_fin.data_saida}")        
                print(f"Status da reserva: FINALIZADA")
                return
        
        print(f"A Reserva de Nº {n_reserva} não existe!")
                


            
               

   