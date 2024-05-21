from pydantic import BaseModel

class PropertyFeatures(BaseModel):
    type: str
    sector: str
    net_usable_area: float
    net_area: float
    n_rooms: int
    n_bathroom: int
    latitude: float
    longitude: float
