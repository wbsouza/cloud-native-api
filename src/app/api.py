from fastapi import FastAPI, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder

from app.settings import configs
from app.model import CommentSchema, UpdateCommentSchema

app = FastAPI(
    title=configs.API_TITLE,
    version=configs.API_VERSION,
    description=configs.API_DESCRIPTION
)


@app.get("/", tags=["Home"])
def get_root() -> dict:
    return {
        "message": configs.API_WELCOME_MESSAGE
    }


comments = [
    {
        "id": 1,
        "name": "Michael",
        "ingredients": ["Let's start a discussion, What is the best API framework in your opinion?"]
    }
]


@app.get("/comment", tags=["Comment"], status_code=status.HTTP_200_OK)
def get_comments() -> dict:
    return {
        "data": comments
    }


@app.get("/comment/{id}", tags=["Comment"], status_code=status.HTTP_200_OK)
def get_comment(id: int) -> dict:
    if id > len(comments) or id < 1:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= "Invalid ID passed.")

    for comment in comments:
        if comment['id'] == id:
            return {
                "data": [
                    comment
                ]
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such comment with ID {} exist".format(id))


@app.post("/comment", tags=["Comment"], status_code=status.HTTP_201_CREATED)
def add_comment(comment: CommentSchema = Body(...)) -> dict:
    comment.id = len(comments) + 1
    comments.append(comment.dict())
    return {
        "message": "Comment added successfully."
    }


@app.put("/comment", tags=["Comment"], status_code=status.HTTP_202_ACCEPTED)
def update_comment(id: int, comment_data: UpdateCommentSchema) -> dict:
    stored_comment = {}
    for comment in comments:
        if comment["id"] == id:
            stored_comment = comment

    if not stored_comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such comment exists.")

    stored_comment_model = CommentSchema(**stored_comment)
    updated_comment = comment_data.dict(exclude_unset=True)
    updated_comment = stored_comment_model.copy(update=update_comment)
    comments[comments.index(stored_comment_model)] = jsonable_encoder(updated_comment)

    return {
        "message": "Comment updated successfully."
    }


@app.delete("/comment/{id}", tags=["Comment"], status_code=status.HTTP_202_ACCEPTED)
def delete_comment(id: int) -> dict:
    if id > len(comments) or id < 1:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= "Invalid ID passed.")

    for comment in comments:
        if comment['id'] == id:
            comments.remove(comment)
            return {
                "message": "Comment deleted successfully."
            }

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such comment with ID {} exist".format(id))
