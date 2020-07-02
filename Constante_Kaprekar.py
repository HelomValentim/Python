#Constante de Kaprekar, um cálculo misterioso que retorna uma constante (6174) em até no maximo 7 ciclos de cálculo, e após chegar neste valor o mesmo se repete infinitamente.

#Como realizar o cálculo?
# 1 Pegue qualquer número natural de 4 dígitos, que tenha no mínimo dois dígitos diferentes (pode lançar mão de zeros à esquerda)
# 2 Arrange os dígitos em ordem ascendente e depois em ordem descendente de forma a obter dois número com quatro dígitos cada. Coloque zeros à esquerda se necessário.
# 3 Subtraia o menor número do maior.
# 4 Volte ao passo dois e processe o resultado.

#Solicitação de input do valor para realizar o cálculo
num = input('\nDigite um número natural de 4 digitos que tenha no mínimo 2 digitos diferentes: ')
constante = int(6174)

#Função para ordenar o número digitado de forma crecente
def ordenarCrecente(entrada):
    lista = list(str(entrada))
    lista.sort()
    valor = ''.join(lista)
    saida = int(valor)
    return(saida)

#Função para ordenar o número digitado de forma decrescente
def ordenarDecrescente(entrada):
    lista = list(str(entrada))
    lista.sort(reverse = True)
    valor = ''.join(lista)
    saida = int(valor)
    return(saida)

#Função que realiza o cálculo de kaprekar e imprime os valores para verificação
def kaprekar(valor):
    numero = int(valor)
    cresc = ordenarCrecente(valor)
    decre = ordenarDecrescente(valor)
    print(f'\nO Número é {numero:04d} \nOrdenado de forma Crecente fica {cresc:04d} \nOrdenado de forma Decrescente fica {decre:04d}')
    resultado = decre - cresc
    print(f'Resultado do Cálculo: {decre:04d} - {cresc:04d} = {resultado:04d}')
    return(resultado)

#Função que realiza o cálculo de kaprekar até que a constante seja alcançada, e no final imprime a quantidade de ciclos necessários para chegar a constante.
def rodarConstante(numero):
    res = numero
    cont = 1
    while res != constante:
        print('-'*120)
        print(f'{cont}º Ciclo de Cálculo')
        valor = kaprekar(res)
        res = valor
        cont = cont + 1

    print('\n')
    print('='*120)
    print(f'Foram necessários {cont - 1} ciclos para achar a constante de Kaprekar')
    print('='*120)
    print('\n')

#Função para verificar se o valor digitado no input pelo usúario atende os requisitos do cálculo como ter 4 digitos e ter pelo menos 2 números diferentes entre sí.
def verificaInput(num_digitado):
    if len(num_digitado) == 4:
        if len(set(num_digitado)) > 1:
            #Chamada da função que realiza o loop para achar a constante, passando como parâmetro o valor do input do usúario.
            rodarConstante(num_digitado)

        else:
            print('\n')
            print('#'*120)
            print('O número digitado deve ter pelo menos 2 números diferentes')
            num = input('\nDigite novamente um número natural de 4 digitos que tenha no mínimo 2 digitos diferentes: ')
            verificaInput(num)

    else:
        print('\n')
        print('#'*120)
        print('O número digitado deve ter 4 digitos')
        num = input('\nDigite novamente um número natural de 4 digitos que tenha no mínimo 2 digitos diferentes: ')
        verificaInput(num)

#Chamada da função para verificar o input e rodar o cálculo.
verificaInput(num)
