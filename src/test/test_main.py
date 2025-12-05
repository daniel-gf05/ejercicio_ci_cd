from src.main import saludo, toUpper, toLower

def test_main():
    assert 'Hola Daniel' in saludo('Daniel')
    
def test_toUpper():
    assert toUpper('daniel') == 'DANIEL'

def test_toLower():
    assert toLower('daniel') == 'DANIEL'