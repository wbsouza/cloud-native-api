from pymongo import MongoClient
from bson import ObjectId
from app.settings import configs

client = MongoClient(
    host=[configs.DB_HOST],
    serverSelectionTimeoutMS=3000  # 3 second timeout
)
database = client[configs.DB_NAME]
comment_collection = database.get_collection('comments_collection')


def parse_comment_data(comment) -> dict:
    return {
        "id": str(comment["_id"]),
        "name": comment["name"],
        "content": comment["content"],
        "replies": comment["replies"]
    }


def save_comment(comment_data: dict) -> dict:
    comment = comment_collection.insert_one(comment_data).inserted_id
    return {
        "id": str(comment)
    }


def get_single_comment(id: str) -> dict:
    comment = comment_collection.find_one({"_id": ObjectId(id)})
    if comment:
        return parse_comment_data(comment)


def get_all_comments() -> list:
    comments = []
    for comment in comment_collection.find():
        comments.append(parse_comment_data(comment))

    return comments


def update_comment_data(id: str, data: dict):
    comment = comment_collection.find_one({"_id": ObjectId(id)})
    if comment:
        comment_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True


def remove_comment(id: str):
    comment = comment_collection.find_one({"_id": ObjectId(id)})
    if comment:
        comment_collection.delete_one({"_id": ObjectId(id)})
        return True
