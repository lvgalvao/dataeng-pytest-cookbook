from src.data_transform import clean_data_lower

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