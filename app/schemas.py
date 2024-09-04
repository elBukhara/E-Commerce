from pydantic import BaseModel
from typing import Optional

class AddItem(BaseModel):
    name: str
    description: Optional[str] = None

class Item(AddItem):
    id: int
