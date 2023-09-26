# api/endpoints.py
# Импортируем класс API роутера.
from fastapi import APIRouter, Body

#from app.schemas.schemas import Person

# Создаём объект роутера.
router = APIRouter()


# В декораторе подставляем объект роутера вместо app.
@router.get('/{name}')
def greetings(
        name:str
        ) -> str:
    return name