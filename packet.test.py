from packet import generate_parity_bit, transpose_columns


def test_generate_parity_bit():
    assert generate_parity_bit([0, 0, 0, 0]) == 0, "Should be 0"
    assert generate_parity_bit([1, 0, 0, 0]) == 1, "Should be 1"
    assert generate_parity_bit([1, 1, 0, 0]) == 0, "Should be 0"
    assert generate_parity_bit([1, 1, 1, 0]) == 1, "Should be 1"
    assert generate_parity_bit([1, 1, 1, 1]) == 0, "Should be 0"


def test_transpose_columns():
    assert transpose_columns([[0, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1], [1, 0, 0, 0]]) == [
        [0, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0]], "Should be transposed"

    assert transpose_columns([[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]) == [
        [1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1]], "Should be transposed"


if __name__ == '__main__':
    test_generate_parity_bit()
    test_transpose_columns()
    print("Testes passaram!")
