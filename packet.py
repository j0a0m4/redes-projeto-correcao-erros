def is_even(number: int) -> bool:
    '''
    is_even verifica se um número é par

    Argumentos:\n
    number: um número inteiro
    '''

    return number % 2 == 0


def is_odd(number: int) -> bool:
    '''
    is_odd verifica se um número é ímpar

    Argumentos:\n
    number: um número inteiro
    '''

    return not is_even(number)


def generate_parity_bit(packet: list) -> int:
    '''
    generate_parity_bit retorna o bit de paridade adequado para um pacote, usando a paridade par

    Argumentos: \n
    packet -- uma lista contendo os bits
    '''
    totalOneBits: int = packet.count(1)

    return int(is_odd(totalOneBits))


def flip_bit(bit: int) -> int:
    '''
    flip_bit muda o bit para sua contraparte

    Argumentos: \n
    bit -- numero inteiro 0 ou 1
    '''
    flipped: bool = not bool(bit)
    return int(flipped)


def add_parity_bit(packet: list) -> list:
    '''
    add_parity_bit retorna uma lista acrescentado do bit de paridade

    Argumentos: \n
    packet -- uma lista contendo os bits
    '''

    return packet.copy() + [generate_parity_bit(packet)]


def remove_parity_bit(packet: list) -> list:
    '''
    remove_parity_bit remove o bit de paridade de uma lista

    Argumentos: \n
    packet -- uma lista contendo os bits
    '''
    return packet[:-1]


def get_parity_bit(packet: list) -> int:
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
    zipped = zip(*packetMatrix)
    return [list(row) for row in zipped]


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
    splitted: list = split_stream(originalPacket)

    columnParity: list = reduce_column_parity_bit(splitted)
    lineParity: list = reduce_line_parity_bit(splitted)

    return lineParity.copy() + [columnParity.copy()]


def remove_line_parity(originalPacket: list) -> list:
    '''
    remove_line_parity remove a linha de paridade da matriz

    Argumentos: \n
    originalPacket -- pacote original a ser codificado na forma de uma lista.
    '''
    return originalPacket[:-1]


def remove_column_parity(originalPacket: list) -> list:
    '''
    remove_column_parity remove a coluna de paridade da matriz

    Argumentos: \n
    originalPacket -- pacote original a ser codificado na forma de uma lista.
    '''
    return [
        remove_parity_bit(packet)
        if len(packet) > 4 else packet
        for packet in originalPacket
    ]


def strip_matrix(codedPacket: list) -> list:
    '''
    strip_matrix remove os bits de paridade dos packets

    Argumentos: \n
    codedPacket -- pacote codificado a ser descriptografado
    '''
    return [
        remove_parity_bit(packet)
        for packet in codedPacket
        if len(packet) > 4
    ]


def get_error_coordinates(codedPacket: list) -> list:
    '''
     get_error_coordinates gera uma lista de tuplas contendo os valores de indíce da linha e da coluna que estão com erro

    Argumentos: \n
    codedPacket -- pacote codificado a ser descriptografado
    '''
    lines: list = transpose_columns(remove_column_parity(codedPacket))
    columns: list = remove_line_parity(codedPacket)

    coordinates: list = []

    for i in range(len(columns)):
        if not check_packet_integrity(columns[i]):
            for j in range(len(lines)):
                if not check_packet_integrity(lines[j]):
                    coordinates.append((i, j))

    return coordinates.copy()


def fix_packet_error(packet: list, index: int) -> list:
    '''
     fix_packet_error altera o bit da list packet no index especificado

    Argumentos: \n
    packet -- pacote codificado
    index -- indice da lista a ter o bit trocado
    '''
    newPacket: list = packet.copy()
    bit: int = newPacket[index]

    newPacket[index] = flip_bit(bit)
    return newPacket


def decode_packet(transmittedPacket: list) -> list:
    '''
    decode_packet gera uma matriz removendo as paridades de linha e coluna do pacote e corrigindo possíveis erros

    Argumentos: \n
    transmittedPacket -- pacote original a ser decodificado
    '''
    splitted: list = split_stream(flat_map(transmittedPacket))
    error_coordinates: list = get_error_coordinates(splitted)
    stripped: list = strip_matrix(splitted)

    storage: list = stripped.copy()

    for i, j in error_coordinates:
        packet: list = stripped[i]
        storage[i] = fix_packet_error(packet, j)
    return storage.copy()


def split_stream(originalPacket: list) -> list:
    '''
    split_stream transforma a lista de packets em uma lista de lista de packets

    Argumentos: \n
    originalPacket -- pacote original a ser transformado
    '''
    splittedPacket: list = []
    while len(originalPacket):
        storage: list = []
        for i in range(len(originalPacket)):
            storage.append(originalPacket.pop())
        splittedPacket.append(storage)
    return splittedPacket


def flat_map(elements: list) -> list:
    '''
    flat_map desaninha as listas dentro da lista de elementos

    Argumentos: \n
    originalPacket -- pacote original a ser transformado
    '''
    flattened: list = []
    for element in elements:
        if type(element) == int:
            flattened.append(element)
        else:
            for num in element:
                flattened.append(num)
    return flattened
