from packet import generate_parity_bit


def test_generate_parity_bit():
    assert generate_parity_bit([1, 1, 0, 0]) == 0, "Should be 0"
    assert generate_parity_bit([1, 0, 0, 0]) == 1, "Should be 1"


if __name__ == '__main__':
    test_generate_parity_bit()
    print("Testes passaram!")
