from src.main import saludo, toUpper

def test_main():
    assert 'Hola Daniel' in saludo('Daniel')
    
def test_toUpper():
    assert toUpper('daniel') == 'DANIEL'