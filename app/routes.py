from flask import Flask, request
from app.database import (
    scan, insert,
    deactivate_user, select
)

app = Flask(__name__)

@app.route("/users")
def get_all_users():
    out = {
        "ok": True,
        "message": "Success",
        "body": scan()
    }
    return out


@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.json
    out = {
        "ok": True,
        "message": "Success",
        "new_id": insert(
            user_data.get("first_name"),
            user_data.get("last_name"),
            user_data.get("hobbies")
        )
    }
    return out, 201


@app.route("/users/<int:pk>", methods=["DELETE"]) # pk stands for Primary Key
def delete_user(pk):
    out = {
        "ok": True,
        "message": "Success"
    }
    deactivate_user(pk)
    return out, 200

@app.route("/users/<int:pk>", methods=["GET"])
def get_single_user(pk):
    out = {
        "ok": True,
        "message": "Success",
        "body": select(pk)
    }
    return out, 200