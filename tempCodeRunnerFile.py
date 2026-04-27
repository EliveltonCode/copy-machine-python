# app-copiadora.py
# Este programa simula um sistema de copiadora, permitindo ao usuário calcular o custo
# de serviços como digitação, impressão colorida, impressão preto e branco e fotocópia.
# Inclui opções para serviços adicionais e descontos baseados na quantidade de páginas.

# Dicionários com os preços dos serviços principais
SERVICOS = {
    'DIG': 1.10,  # Digitação: R$ 1,10 por página
    'ICO': 1.0,   # Impressão Colorida: R$ 1,00 por página
    'IPB': 0.40,  # Impressão Preto e Branco: R$ 0,40 por página
    'FOT': 0.20,  # Fotocópia: R$ 0,20 por página
}

# Dicionários com os preços dos serviços adicionais
ADICIONAL = {
    '0': 0.00,  # Sem adicional
    '1': 10.00, # Encadernação Simples: R$ 10,00
    '2': 25.00  # Encadernação com Capa Dura: R$ 25,00
}

# Dicionários com as porcentagens de desconto baseadas na quantidade de páginas
DESCONTO = {
    '10-99': 0.10,   # 10% de desconto para 10-99 páginas
    '100-999': 0.15, # 15% de desconto para 100-999 páginas
    '1000+': 0.20    # 20% de desconto para 1000+ páginas
}

def menu() -> str:
    """
    Exibe o menu de boas-vindas e opções de serviços disponíveis.
    
    Returns:
        str: A string do menu a ser exibida.
    """
    return (f'Bem vindo a Copiadora do Python\n'
          'Entre com o tipo de serviço desejado\n' \
          'DIG - Digitação\n'
          'ICO - Impressão Colorida\n'
          'IPB - Impressão Preto e Branco\n' \
          'FOT - Fotocópia\n')

def escolher_servico() -> float:
    """
    Solicita ao usuário a escolha do serviço e valida a entrada.
    
    Returns:
        float: O preço do serviço selecionado.
    """
    while True:
        servico = input('Digite a sigla do serviço desejado: ').upper().strip()
        if servico not in SERVICOS:
            print('Opção inválida. Por favor, escolha uma opção válida.')
            continue
        return SERVICOS[servico]

def servico_adicional() -> float:
    """
    Solicita ao usuário a escolha de um serviço adicional e valida a entrada.
    
    Returns:
        float: O preço do serviço adicional selecionado.
    """
    print(f'Deseja adicionar mais algum serviço ao pedido?\n'
            '1 - Encadernação Simples - R$10,00\n'
            '2 - Encadernação com Capa Dura - R$25,00\n'
            '0 - Sair sem adicionar serviço adicional')
    
    while True:
        adicional = input('Digite o número correspondente ao serviço adicional desejado: ').strip()

        if adicional not in ADICIONAL:
            print('Opção inválida. Por favor, escolha uma opção válida.')
            continue

        return ADICIONAL[adicional]

def numero_de_paginas() -> int:
    """
    Solicita ao usuário a quantidade de páginas e valida a entrada.
    
    Returns:
        int: O número de páginas inserido pelo usuário.
    """
    while True:
        quantidade = input('Digite a quantidade de páginas: ').strip()
        try:
            quantidade = int(quantidade)
            if quantidade <= 0 or quantidade >= 10000:
                print('Quantidade inválida. Por favor, digite um número inteiro entre (1 e 10.000)')
                continue
            else:
                return quantidade
        except ValueError:
            print('Entrada inválida. Por favor, digite um número inteiro válido.')

def porcentagem_do_desconto(numero_de_paginas) -> float:
    """
    Calcula a porcentagem de desconto baseada na quantidade de páginas.
    
    Args:
        numero_de_paginas (int): O número de páginas.
    
    Returns:
        float: A porcentagem de desconto aplicável.
    """
    if numero_de_paginas < 10:
        return 0.0
    elif numero_de_paginas >= 10 and numero_de_paginas < 100:
        return DESCONTO['10-99']
    elif numero_de_paginas >= 100 and numero_de_paginas < 1000:
        return DESCONTO['100-999']
    elif numero_de_paginas >= 1000:
        return DESCONTO['1000+']

def calcular_total(servico, paginas, desconto, adicional):
    """
    Calcula o total do pedido incluindo serviço, desconto e adicional.
    
    Args:
        servico (float): Preço por página do serviço.
        paginas (int): Número de páginas.
        desconto (float): Porcentagem de desconto.
        adicional (float): Valor adicional.
    
    Returns:
        float: O total a pagar.
    """
    valor_servico = servico * paginas
    valor_desconto = desconto * valor_servico
    return valor_servico + adicional - valor_desconto

def main():
    """
    Função principal que executa o fluxo do programa: exibe menu, coleta dados e calcula o total.
    """
    print(menu())
    servico = escolher_servico()
    paginas = numero_de_paginas()
    adicional = servico_adicional()
    desconto = porcentagem_do_desconto(paginas)
    valor_desconto = desconto * (servico * paginas)
    total = calcular_total(servico, paginas, desconto, adicional)
    print('Resumo do pedido:')
    print(f'Total R${total:.2f}')
    print(f'Serviço: R${(servico * paginas):.2f}')
    print(f'Desconto: R${valor_desconto:.2f}')
    print(f'Número de páginas: {paginas}')
    print(f'Valor adicional: R${adicional:.2f}')
    print('Obrigado por escolher a Copiadora do Python!')

if __name__ == "__main__":
    main()  