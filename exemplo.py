import requests
from pydantic import BaseModel

      # requests.get #select
      # requests.post #create
      # requests.put # update
      # requests.delete #delete
    # response = requests.get(url="https://www.mercadolivre.com.br/")
    # print(response.text)


url = "https://pokeapi.co/api/v2/pokemon/25"
response = requests.get(url)
data = response.json()
data_types = data['types']  # Supondo que 'data' é o dicionário com os dados do Pokémon
types_list = []
for type_info in data_types:
    types_list.append(type_info['type']['name'])
types = ', '.join(types_list) #Transforma uma lista/dict em uma linha
print(data['name'], types)