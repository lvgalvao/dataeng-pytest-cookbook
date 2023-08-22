from pytest import mark
from src.data_transform_05 import clean_data_lower

"""
Todo teste é formado por 3 etapas
1. Given: Onde você prepara o ambiente para o teste
2. When: Onde você executa o código que você quer testar
3. Then: Onde você verifica se o resultado é o esperado

"""
@mark.smoke
def test_data_transform_clean_data_lower():
    # Given
    data_list = "LUCIANO"
    expected = "luciano"

    # When
    result = clean_data_lower(data_list)

    # Then
    assert result == expected

@mark.smoke
def test_data_transform_clean_data_lower_empty():
    # Given
    data_list = ""
    expected = ""

    # When
    result = clean_data_lower(data_list)

    # Then
    assert result == expected

@mark.chefe
@mark.smoke
def test_data_transform_clean_data_lower_and_spaces():
    # Given
    data_list = "    CHEFE    "
    expected = "chefe"

    # When
    result = clean_data_lower(data_list)

    # Then
    assert result == expected