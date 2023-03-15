from typing import List, Optional

from pydantic import BaseModel, Field, validator

from app.models.domain.items import Item
from app.models.schemas.rwschema import RWSchema

DEFAULT_ITEMS_LIMIT = 20
DEFAULT_ITEMS_OFFSET = 0


class ItemForResponse(RWSchema, Item):
    tags: List[str] = Field(..., alias="tagList")

    @validator("image")
    def image_must_not_empty(cls, v):
        if not v:
            v = "placeholder.png"
        return v


class ItemInResponse(RWSchema):
    item: ItemForResponse


class ItemInCreate(RWSchema):
    title: str
    description: str
    body: Optional[str] = None
    image: Optional[str] = None
    tags: List[str] = Field([], alias="tagList")


class ItemInUpdate(RWSchema):
    title: Optional[str] = None
    description: Optional[str] = None
    body: Optional[str] = None
    image: Optional[str] = None
    tags: Optional[List[str]] = Field(None, alias="tagList")


class ListOfItemsInResponse(RWSchema):
    items: List[ItemForResponse]
    items_count: int


class ItemsFilters(BaseModel):
    tag: Optional[str] = None
    seller: Optional[str] = None
    favorited: Optional[str] = None
    limit: int = Field(DEFAULT_ITEMS_LIMIT, ge=1)
    offset: int = Field(DEFAULT_ITEMS_OFFSET, ge=0)
