from cliente import Cliente
from quarto import Quarto
from reserva import Reserva
from hotel import Hotel

# Função para exibir o menu
def exibir_menu():
    print("----------- MENU HOTEL ------------")
    print("\033[31mOPÇÃO 0: ENCERRAR\033[0m")
    print("OPÇÃO 1: Adicionar Quarto")
    print("OPÇÃO 2: Criar Reserva")
    print("OPÇÃO 3: Finalizar Reserva")
    print("OPÇÃO 4: Pesquisar Reserva")

# Função principal
def main():
    hotel = Hotel()  # Instancia o hotel
    opcao = None

    while opcao != 0:
        exibir_menu()  # Exibe o menu a cada iteração
        opcao = int(input("SELECIONAR: "))
        
        if opcao == 1:
            # Adicionar Quarto
            numero = int(input("Digite o número do quarto: "))
            tipo_quarto = int(input("Digite o tipo do quarto (1: Suíte Presidencial, 2: Suíte com varanda, 3: Suíte, 4: Quarto Simples): "))
            preco = int(input("Digite o preço do quarto: "))
            quarto = Quarto(numero=numero, tipo_quarto=tipo_quarto, preco=preco)
            hotel.add_quarto(quarto)
            print(f"Quarto {numero} adicionado com sucesso!")

        elif opcao == 2:
            # Criar Reserva
            nome = input("Nome do cliente: ")
            idade = int(input("Idade do cliente: "))
            cpf = int(input("CPF do cliente: "))
            forma_pagamento = input("Forma de pagamento: ")
            num_quarto = int(input("Número do quarto para reservar: "))
            data_entrada = input("Data de entrada (ex: 2024-09-10): ")
            data_saida = input("Data de saída (ex: 2024-09-15): ")

            cliente = Cliente(nome=nome, idade=idade, cpf=cpf, forma_pagamento=forma_pagamento, num_quarto=num_quarto)
            
            # Procurar quarto no hotel
            quarto_encontrado = None
            for quarto in hotel.quartos:
                if quarto.numero == num_quarto:
                    quarto_encontrado = quarto
                    break

            if quarto_encontrado and hotel.verificar_disponibilidade_quarto(quarto_encontrado):
                hotel.criar_reserva(data_entrada, data_saida, quarto_encontrado, cliente)
            else:
                print(f"Quarto {num_quarto} não está disponível ou não existe.")

        elif opcao == 3:
            # Finalizar Reserva
            n_reserva = int(input("Digite o número da reserva a ser finalizada: "))
            hotel.finalizar_reserva(n_reserva)
            print(f"Reserva nº {n_reserva} finalizada!")

        elif opcao == 4:
            # Pesquisar Reserva
            n_reserva = int(input("Digite o número da reserva a ser pesquisada: "))
            hotel.pesquisar_reserva(n_reserva)

        elif opcao == 0:
            # Encerrar o programa
            print("Encerrando o sistema do hotel...")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
