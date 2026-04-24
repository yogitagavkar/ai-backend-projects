from pydantic import BaseModel, Field
from typing import List, Optional

class OrderItem(BaseModel):
    name: str = Field(..., example="Paneer Tikka")
    qty: int = Field(..., gt=0, example=2)
    unit_price: float = Field(..., gt=0, example=400)
    modifiers: List[str] = Field(default_factory=list, example=["less spicy"])
    line_total: float = Field(..., example=800)


class BillResponse(BaseModel):
    items: List[OrderItem]
    subtotal: float
    tax: float
    tip: float
    discounts: float
    total: float


class ChatRequest(BaseModel):
    user_input: str = Field(..., example="2 paneer tikka less spicy")


class ChatResponse(BaseModel):
    response: Optional[str] = None
    bill: Optional[BillResponse] = None