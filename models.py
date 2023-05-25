from pydantic import BaseModel

class Movie(BaseModel):
    name: str
    watched: bool


class SerializedMovie(Movie):
    series: str
    index: int