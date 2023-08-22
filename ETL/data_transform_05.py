
def clean_data_lower(raw_string: str) -> str:
    """
    Função que limpa uma string retirando espaços e deixando tudo em minúsculo.

    Args:
        Uma string
    
    Returns:
        Uma string tratada
    
    Examples:
        >>> clean_data_lower("    LUCIANO")
        "luciano"
        >>> clean_data_lower("    PYTHON    ")
        "python"
    """
    result = raw_string.strip().lower()
    
    return result