from src.data_transform import clean_data_lower

"""
Todo teste é formado por 3 etapas
1. Given: Onde você prepara o ambiente para o teste
2. When: Onde você executa o código que você quer testar
3. Then: Onde você verifica se o resultado é o esperado

"""
def test_data_transform_clean_data_lower():
    # Given
    data_list = ['  A', 'B  ', '  C  ']
    expected = ['a', 'b', 'c']

    # When
    result = clean_data_lower(data_list)

    # Then
    assert result == expected