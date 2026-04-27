# App Copiadora

Este é um projeto simples em Python que simula um sistema de copiadora. O programa permite ao usuário calcular o custo de serviços de impressão e cópia, incluindo opções para serviços adicionais e descontos baseados na quantidade de páginas.

## Funcionalidades

- **Serviços Disponíveis**:
  - DIG: Digitação (R$ 1,10 por página)
  - ICO: Impressão Colorida (R$ 1,00 por página)
  - IPB: Impressão Preto e Branco (R$ 0,40 por página)
  - FOT: Fotocópia (R$ 0,20 por página)

- **Serviços Adicionais**:
  - 0: Sem adicional
  - 1: Encadernação Simples (R$ 10,00)
  - 2: Encadernação com Capa Dura (R$ 25,00)

- **Descontos**:
  - Menos de 10 páginas: Sem desconto
  - 10-99 páginas: 10% de desconto
  - 100-999 páginas: 15% de desconto
  - 1000+ páginas: 20% de desconto

## Como Executar

1. Certifique-se de ter Python instalado no seu sistema (versão 3.x recomendada).
2. Baixe ou clone o repositório.
3. Execute o arquivo `app-copiadora.py`:
   ```
   python app-copiadora.py
   ```
4. Siga as instruções no terminal para selecionar o serviço, quantidade de páginas e serviços adicionais.

## Estrutura do Código

- `SERVICOS`: Dicionário com os preços dos serviços principais.
- `ADICIONAL`: Dicionário com os preços dos serviços adicionais.
- `DESCONTO`: Dicionário com as porcentagens de desconto.
- `menu()`: Exibe o menu de boas-vindas.
- `escolher_servico()`: Solicita e valida a escolha do serviço.
- `servico_adicional()`: Solicita e valida a escolha do serviço adicional.
- `numero_de_paginas()`: Solicita e valida a quantidade de páginas.
- `porcentagem_do_desconto()`: Calcula o desconto baseado na quantidade de páginas.
- `calcular_total()`: Calcula o total do pedido.
- `main()`: Função principal que coordena o fluxo do programa.

## Exemplo de Uso

```
Bem vindo a Copiadora do Python
Entre com o tipo de serviço desejado
DIG - Digitação
ICO - Impressão Colorida
IPB - Impressão Preto e Branco
FOT - Fotocópia

Digite a sigla do serviço desejado: IPB
Digite a quantidade de páginas: 150
Deseja adicionar mais algum serviço ao pedido?
1 - Encadernação Simples - R$10,00
2 - Encadernação com Capa Dura - R$25,00
0 - Sair sem adicionar serviço adicional
Digite o número correspondente ao serviço adicional desejado: 1

Resumo do pedido:
Total R$51.00
Serviço: R$60.00
Desconto: R$9.00
Número de páginas: 150
Valor adicional: R$10.00
Obrigado por escolher a Copiadora do Python!
```

## Requisitos

- Python 3.x

## Decisões de Implementação

- Utilizei dicionários para facilitar a manutenção dos preços e evitar estruturas condicionais complexas.
- Separei a lógica em funções para melhorar a organização e reutilização do código.
- Implementei validação de entrada para evitar erros do usuário.

## Aprendizados

- Validação de entrada com try/except
- Uso de dicionários para estrutura de dados
- Organização de código

## Autor

Elivelton Rodrigues dos Santos - Projeto de portfólio.