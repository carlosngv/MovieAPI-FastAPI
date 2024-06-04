from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2023) # ? Que tenga valores menor a 2024
    rating: float = Field()
    category: str

    class Config:
        json_schema_extra = {
            'example': {
                'id': 1,
                'title': 'Movie title',
                'overview': 'Movie description',
                'year': 2023,
                'rating': 5.0,
                'category': 'Action'
            }
        }
