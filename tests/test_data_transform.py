from src.data_transform import clean_data_lowe

"""
Todo teste é formado por 3 etapas
1. Given: Onde você prepara o ambiente para o teste
2. When: Onde você executa o código que você quer testar
3. Then: Onde você verifica se o resultado é o esperado

"""
def test_data_transform_clean_data_lower():
    # Given
    entrada = "PYTHON"
    esperado = "python"

    # When
    resultado = clean_data_lowe(entrada)

    # Then
    assert resultado == esperado

def test_data_transform_clean_data_lower_com_espacos():
    # Given
    entrada = "   HELLO WORLD   "
    esperado = "hello world"

    # When
    resultado = clean_data_lowe(entrada)

    # Then
    assert resultado == esperado