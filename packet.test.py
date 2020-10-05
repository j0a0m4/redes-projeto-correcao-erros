from packet import generate_parity_bit, transpose_columns, add_parity_bit, check_packet_integrity


def should_generate_parity_bit():
    assert generate_parity_bit([0, 0, 0, 0]) == 0, "Should be 0"
    assert generate_parity_bit([1, 0, 0, 0]) == 1, "Should be 1"
    assert generate_parity_bit([1, 1, 0, 0]) == 0, "Should be 0"
    assert generate_parity_bit([1, 1, 1, 0]) == 1, "Should be 1"
    assert generate_parity_bit([1, 1, 1, 1]) == 0, "Should be 0"


def should_add_parity_bit():
    assert add_parity_bit([0, 0, 0, 0]) == [
        0, 0, 0, 0, 0], "Should add parity bit 0"
    assert add_parity_bit([1, 0, 0, 0]) == [
        1, 0, 0, 0, 1], "Should add parity bit 1"
    assert add_parity_bit([1, 1, 0, 0]) == [
        1, 1, 0, 0, 0], "Should add parity bit 0"
    assert add_parity_bit([1, 1, 1, 0]) == [
        1, 1, 1, 0, 1], "Should add parity bit 1"
    assert add_parity_bit([1, 1, 1, 1]) == [
        1, 1, 1, 1, 0], "Should add parity bit 0"


def should_check_packet_integrity():
    assert check_packet_integrity([0, 0, 0, 0, 0]) == True, "Should be True"
    assert check_packet_integrity([0, 0, 0, 0, 1]) == False, "Should be False"
    assert check_packet_integrity([1, 0, 0, 0, 1]) == True, "Should be True"
    assert check_packet_integrity([1, 0, 0, 0, 0]) == False, "Should be False"
    assert check_packet_integrity([1, 1, 0, 0, 0]) == True, "Should be True"
    assert check_packet_integrity([1, 1, 0, 0, 1]) == False, "Should be False"
    assert check_packet_integrity([1, 1, 1, 0, 1]) == True, "Should be True"
    assert check_packet_integrity([1, 1, 1, 0, 0]) == False, "Should be False"
    assert check_packet_integrity([1, 1, 1, 1, 0]) == True, "Should be True"
    assert check_packet_integrity([1, 1, 1, 1, 1]) == False, "Should be False"


def should_transpose_columns():
    assert transpose_columns([[0, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1], [1, 0, 0, 0]]) == [
        [0, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0]], "Should be transposed"

    assert transpose_columns([[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]) == [
        [1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1]], "Should be transposed"


if __name__ == '__main__':
    should_generate_parity_bit()
    should_add_parity_bit()
    should_check_packet_integrity()
    should_transpose_columns()
    print("Testes passaram!")
