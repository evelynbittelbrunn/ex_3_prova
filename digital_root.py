def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def test_digital_root():
    assert digital_root(0) == 0
    assert digital_root(7) == 7
    
    assert digital_root(16) == 7
    assert digital_root(49) == 4

    assert digital_root(942) == 6
    assert digital_root(132189) == 6
    assert digital_root(493193) == 2
    
    assert digital_root(123456789) == 9

if __name__ == "__main__":
    test_digital_root()
    print("TESTES APROVADOS")
