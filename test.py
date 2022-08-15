def test_sum():
    a = 2
    b = 2
    count = a+b
    assert count == 4, f'Expected: OWASP Juice Shop \n Actual: {count}'

def test_min():
    a = 2
    b = 1
    count = a-b
    assert count == 1, f'Expected: OWASP Juice Shop \n Actual: {count}'