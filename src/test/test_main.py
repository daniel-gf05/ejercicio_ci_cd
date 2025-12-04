from src.main import saludo

def test_main():
    assert 'Hola Daniel' in saludo('Daniel')