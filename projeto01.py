produtos = {
    {'id': 1, 'nome': 'Notebook', 'preco': 3000},
    {'id': 2, 'nome': 'Processador', 'preco': 1000},
    {'id': 3, 'nome': 'Fonte', 'preco': 300},
    {'id': 4, 'nome': 'Placa de vídeo', 'preco': 2000},
    {'id': 5, 'nome': 'Memória RAM', 'preco': 200}
}


carrinho = []

def exibirOpcoes():
    print('1 - Adicionar item')
    print('2 - Remover item')
    print('3 - Exibir itens e total')
    print('4 - Limpar carrinho')
    print('5 - Sair')

def exibirProdutos():
    for p in produtos:
        print('Código - {0} - Nome {1} - Preço {2}\n'.format(p['id'], p['nome'], p['preco']))

opcao = '1'

print('***** Carrinho de Comprar *****\n')

while opcao != '5':
    exibirOpcoes()
    opcao = input('Digite a opção: ')

    if opcao == '1':
        exibirProdutos()
        id = int(input('Digite o código do item'))
        qtd = int(input('Digite a quantidade'))
        carrinho.append({'id': id, 'quantidade': qtd})

    if opcao == '2':
        id = int(input('Digite o código do item'))

