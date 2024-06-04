from pydantic import BaseModel

class PokemonSchema(BaseModel): #contrato de dados , schema de dados ou view da api
    name: str
    type: str

    class Config:
        orm_mode = True