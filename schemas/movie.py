from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int]= None
    title: str = Field(min_length=5,max_length=15)
    overview: str = Field(min_length=15,max_length=50)
    year: int = Field(le=2024)
    rating: float = Field(le=10, ge=1)
    category: str = Field(min_length=5,max_length=15)

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "title":"Mí película",
                "overview":"Mi descripción",
                "year":2022,
                "rating":8.0,
                "category":"Acción"
            }
        }