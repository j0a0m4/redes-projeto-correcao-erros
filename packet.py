from functools import reduce


def is_even(number: int) -> bool:
    '''
    is_even verifica se um número é par

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

    if is_even(totalOneBits):
        return 0
    else:
        return 1


def add_parity_bit(packet: list) -> list:
    '''
    add_parity_bit retorna uma lista acrescentado do bit de paridade

    Argumentos: \n
    packet -- uma lista contendo os bits
    '''
    newPacket: list = packet.copy()
    newPacket.append(generate_parity_bit(packet))
    return newPacket


def get_parity_bit(packet: list) -> bool:
    '''
    get_parity_bit retorna o bit de paridade de um packet (último elemento da lista)

    Argumentos: \n
    packet -- uma lista contendo os bits
    '''
    return packet[-1]


def get_actual_packet(packet: list) -> list:
    '''
    get_actual_packet o packet sem o bit de paridade (último elemento da lista) sem

    Argumentos: \n
    packet -- uma lista contendo os bits
    '''
    return packet[:-1]


def check_packet_integrity(packet: list) -> bool:
    '''
    check_packet_integrity retorna se um pacote está integro u não

    Argumentos: \n
    packet -- uma lista contendo os bits
    '''
    parityBit: int = get_parity_bit(packet)
    actualPacket: list = get_actual_packet(packet)
    return generate_parity_bit(actualPacket) == parityBit


def transpose_columns(packetMatrix: list) -> list:
    '''
    transpose_columns transforma as colunas de uma matriz nas linhas de uma matriz

    Argumentos: \n
    packetMatrix -- uma lista de listas (matriz)
    '''
    height: int = len(packetMatrix)
    width: int = len(packetMatrix[0])

    return [
        [packetMatrix[j][i] for j in range(height)]
        for i in range(width)
    ]


def reduce_line_parity_bit(packetMatrix: list) -> list:
    '''
    reduce_line_parity_bit adiciona um bit de paridade a cada linha de uma matriz

    Argumentos: \n
    packetMatrix -- uma lista de listas (matriz)
    '''
    return [
        add_parity_bit(packet)
        for packet in packetMatrix
    ]


def reduce_column_parity_bit(packetMatrix: list) -> list:
    '''
    reduce_column_parity_bit gera uma lista contendo as paridades de coluna

    Argumentos: \n
    packetMatrix -- uma lista de listas (matriz)
    '''
    return [
        generate_parity_bit(packet)
        for packet in transpose_columns(packetMatrix)
    ]


def code_packet(originalPacket: list) -> list:
    '''
    code_packet gera uma matriz contendo as paridades de linha e coluna do pacote

    Argumentos: \n
    originalPacket -- pacote original a ser codificado na forma de uma lista.
    '''

    columnParity: list = reduce_column_parity_bit(originalPacket)
    lineParity: list = reduce_line_parity_bit(originalPacket)

    encodedPacket: list = lineParity.copy()
    encodedPacket.append(columnParity)

    return encodedPacket
