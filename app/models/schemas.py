from pydantic import BaseModel

class CopyRequest(BaseModel):
    product_description: str
    platform: str
    persona: str


class ImageRequest(BaseModel):
    product_description: str