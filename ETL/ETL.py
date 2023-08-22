import requests

def extrai_pokemon_da_API_usando_o_nome(number):
    """Retorna o nome do Pokemon a partir do número"""
    url = f"https://pokeapi.co/api/v2/pokemon/{number}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["name"]
    else:
        return None
    
def transform_pokemon_name_in_UPPER_CASE(name):
    """Transforma o nome do Pokemon em letras maiúsculas"""
    return name.upper()

def load_into_txt_file_as_append(pokemon_name):
    """Carrega o nome do Pokemon em um arquivo txt"""
    with open("pokemon.txt", "a") as file:
        file.write(pokemon_name + "\n")

        def test_data_transform_clean_data_lower_and_spaces():
    # Given
    data_list = "    PyTest    "
    expected = "pytest"

    # When
    result = clean_data_lower(data_list)

    # Then
    assert result == expected