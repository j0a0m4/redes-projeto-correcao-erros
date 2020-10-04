from functools import reduce


def isEven(number: int) -> bool:
    '''
    isEven verifica se um número é par

    Argumentos:\n
    number: um número inteiro
    '''
    return number % 2 == 0


def count_one_bit(accumulator: int, bit: int) -> int:
    '''
    count_one_bit é um reducer que conta o número de bits 1 de uma lista

    Argumentos: \n
    accumulator -- o total de bits um da lista, começa com o primeiro elemento \n
    bit -- o bit atual da lista
    '''
    if bit == 1:
        return accumulator + 1
    else:
        return accumulator


def generate_parity_bit(packet: list) -> bool:
    '''
        generate_parity_bit retorna o bit de paridade adequado para um pacote, usando a paridade par

        Argumentos: \n
        packet -- uma lista contendo os bits
    '''
    totalOneBits: int = reduce(count_one_bit, packet)

    if isEven(totalOneBits):
        return 0
    else:
        return 1