from pydantic import BaseModel, Field
from typing import Optional, List


class BaseCommentSchema(BaseModel):
    id: Optional[int]
    name: str = Field(...)
    content: str = Field(...)


class CommentSchema(BaseCommentSchema):

    replies: List[BaseCommentSchema] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Joseph",
                "content": ["This is my initial comment"],
                "replies": [
                    {
                        "name": "Marcus",
                        "content": "And this is my reply :-)"
                    }
                ]
            }
        }


class UpdateCommentSchema(BaseModel):
    name: Optional[str]
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "George",
                "content": "And this is my reply with amendments :-)"
            }
        }


