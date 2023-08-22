from typing import List

def clean_data_lower(data_list: List[str]) -> List[str]:
    """
    Função que limpa os dados e deixa tudo em minúsculo

    Args:
        data_list (List[str]): Lista de dados
    
    Returns:
        List[str]: Lista de dados limpos e em minúsculo
    
    Examples:
        >>> clean_data_lower(['  A', 'B  ', '  C  '])
        ['a', 'b', 'c']
    """
    
    cleaned_data = []
    
    for item in data_list:
        cleaned_item = item.strip().lower()
        cleaned_data.append(cleaned_item)
    
    return cleaned_data
