class Restaurante:
    def __init__(self, nome):
        # Atributo nome do restaurante
        self.nome = nome
        # Definindo um cardápio com preços entre R$ 10,00 e R$ 40,00
        self.cardapio = {
            'Prato Simples': 10,
            'Prato Executivo': 20,
            'Prato Gourmet': 30,
            'Prato Premium': 40
        }

    def apresenta(self):
        # Método para apresentar o restaurante e mostrar o cardápio
        print(f"Bem-vindo ao restaurante {self.nome}!")
        print("Nosso cardápio possui os seguintes pratos:")
        for prato, preco in self.cardapio.items():
            print(f"- {prato}: R${preco}")
        
        # Exibindo explicação sobre Pipeline
        print(f"\n1: Uma pipeline é uma série de etapas encadeadas onde a saída de uma etapa é a entrada para a próxima. Utilizando para automação e processamento eficiente em diferentes contextos.")
        
        # Descrição dos requisitos funcionais e não funcional
        print("\n2: Os requisitos funcionais do restaurante incluem a captura de pedidos, processamento de pagamentos e entrega eficiente dos pratos e as não funcionais eu não lembro.")

    def verificar_paridade(self, numero):
        # Método para verificar se o número é par ou ímpar
        if numero % 2 == 0:
            return f"{numero} é par"
        else:
            return f"{numero} é ímpar"


# Criando uma instância do restaurante
restaurante = Restaurante("Saboroso")

# Chamando a função apresenta() para mostrar o restaurante
restaurante.apresenta()

# Chamando a função verificar_paridade()
print(restaurante.verificar_paridade(7))  # Saída: 7 é ímpar
print(restaurante.verificar_paridade(90))  # Saída: 90 é par

      # Descrição dos requisitos do "Modelo Cascata"
print("\n3: Linearidade, Foco na Documentação Completa, Rigor e Controle de Qualidade, Gestão Predictiva, Estabilidade dos Requisitos.")


