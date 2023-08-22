from modulo.data_transform import limpando_dados_lower

"""
Todo teste é formado por 3 etapas
1. Given: Onde você prepara o ambiente para o teste
2. When: Onde você executa o código que você quer testar
3. Then: Onde você verifica se o resultado é o esperado

"""
def test_data_transform_clean_data_lower():
    # Given
    entrada = "LUCIANO"
    esperado = "luciano"

    # When
    resultado = limpando_dados_lower(entrada)

    # Then
    assert resultado == esperado