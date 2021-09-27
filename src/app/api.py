from fastapi import FastAPI, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder

from app import db
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


@app.get("/comment", tags=["Comment"], status_code=status.HTTP_200_OK)
def get_comments() -> dict:
    comments = db.get_all_comments()
    return {
        "data": comments
    }


@app.get("/comment/{id}", tags=["Comment"], status_code=status.HTTP_200_OK)
def get_comment(id: int) -> dict:
    comment = db.get_single_comment(id)
    if comment:
        return {
            'data': comment
        }
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Invalid ID passed.")


@app.post("/comment", tags=["Comment"], status_code=status.HTTP_201_CREATED)
def add_comment(comment: CommentSchema = Body(...)) -> dict:
    new_comment = db.save_comment(comment.dict())
    return new_comment


@app.put("/comment", tags=["Comment"], status_code=status.HTTP_202_ACCEPTED)
def update_comment(id: int, comment_data: UpdateCommentSchema) -> dict:
    if not db.get_single_comment(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such comment exists.")
    db.update_comment_data(id, comment_data.dict())
    return {
        "message": "Comment updated successfully."
    }


@app.delete("/comment/{id}", tags=["Comment"], status_code=status.HTTP_202_ACCEPTED)
def delete_comment(id: int) -> dict:
    if not db.get_comment_recipe(id):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= "Invalid ID passed.")

    db.remove_comment(id)
