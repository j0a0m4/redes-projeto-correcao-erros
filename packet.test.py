from packet import *


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


def should_remove_parity_bit():
    assert remove_parity_bit([0, 0, 0, 0, 0]) == [
        0, 0, 0, 0], "Should remove parity bit"
    assert remove_parity_bit([1, 0, 0, 0, 1]) == [
        1, 0, 0, 0], "Should remove parity bit"
    assert remove_parity_bit([1, 1, 0, 0, 1]) == [
        1, 1, 0, 0], "Should remove parity bit"
    assert remove_parity_bit([1, 1, 1, 0, 1]) == [
        1, 1, 1, 0], "Should remove parity bit"
    assert remove_parity_bit([1, 1, 1, 1, 0]) == [
        1, 1, 1, 1], "Should remove parity bit"


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
    assert transpose_columns([
        [0, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0]
    ]) == [
        [0, 1, 1, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 1, 0]
    ], "Should be transposed"

    assert transpose_columns([
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]) == [
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 1]
    ], "Should be transposed"


def should_reduce_line_parity_bit():
    assert reduce_line_parity_bit([
        [0, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0]
    ]) == [
        [0, 1, 1, 0, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1]
    ], "Should have simple parity bit"

    assert reduce_line_parity_bit([
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 0, 1, 0]
    ]) == [
        [0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 0, 0]
    ], "Should have simple parity bit"


def should_reduce_column_parity_bit():
    assert reduce_column_parity_bit([
        [0, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0]
    ]) == [1, 1, 1, 1], "Should create parity bit column list"

    assert reduce_column_parity_bit([
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 0]
    ]) == [0, 1, 0, 1], "Should create parity bit column list"


def should_code_packet():
    assert code_packet([
        [0, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0]
    ]) == [
        [0, 1, 1, 0, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1]

    ], "Should encode packet"

    assert code_packet([
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 0]
    ]) == [
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1]

    ], "Should encode packet"

    assert code_packet([
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 1, 0]
    ]) == [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1]

    ], "Should encode packet"

    assert code_packet([
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 1, 1]
    ]) == [
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 1]
    ], "Should encode packet"


def should_remove_line_parity():
    assert remove_line_parity([
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 1]
    ]) == [
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1]
    ], "Should remove line parity"

    assert remove_line_parity([
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1]
    ]) == [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
    ], "Should remove line parity"

    assert remove_line_parity([
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1]
    ]) == [
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0]
    ], "Should remove line parity"

    assert remove_line_parity([
        [0, 1, 1, 0, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1]
    ]) == [
        [0, 1, 1, 0, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
    ], "Should remove line parity"


def should_remove_column_parity():
    assert remove_column_parity([
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 1]
    ]) == [
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [1, 0, 0, 1]
    ], "Should remove column parity"

    assert remove_column_parity([
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1]
    ]) == [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 1, 0],
        [1, 0, 0, 1]
    ], "Should remove column parity"

    assert remove_column_parity([
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1]
    ]) == [
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1]
    ], "Should remove column parity"

    assert remove_column_parity([
        [0, 1, 1, 0, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1]
    ]) == [
        [0, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 1, 1]
    ], "Should remove column parity"


def should_flip_bit():
    assert flip_bit(1) == 0, "Should flip bit"
    assert flip_bit(0) == 1, "Should flip bit"


if __name__ == '__main__':
    should_generate_parity_bit()
    should_flip_bit()
    should_add_parity_bit()
    should_remove_parity_bit()
    should_check_packet_integrity()
    should_transpose_columns()
    should_reduce_line_parity_bit()
    should_reduce_column_parity_bit()
    should_code_packet()
    should_remove_line_parity()
    should_remove_column_parity()
    print("Testes passaram!")
