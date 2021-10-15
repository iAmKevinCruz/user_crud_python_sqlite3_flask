from flask import Flask, request
from app.database import user, vehicle

app = Flask(__name__)

@app.route("/users")
def get_all_users():
    out = {
        "ok": True,
        "message": "Success",
        "body": user.scan()
    }
    return out


@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.json
    out = {
        "ok": True,
        "message": "Success",
        "new_id": user.insert(
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
    user.deactivate_user(pk)
    return out, 200

@app.route("/users/<int:pk>", methods=["GET"])
def get_single_user(pk):
    out = {
        "ok": True,
        "message": "Success",
        "body": user.select(pk)
    }
    return out, 200


@app.route("/vehicles")
def get_all_vehicles():
    out = {
        "ok": True,
        "message": "Success",
        "body": vehicle.scan()
    }
    return out

@app.route("/vehicles", methods=["POST"])
def create_vehicle():
    vehicle_data = request.json
    out = {
        "ok": True,
        "message": "Success",
        "new_id": vehicle.insert(
            vehicle_data.get("license_plate"),
            vehicle_data.get("v_type"),
            vehicle_data.get("color"),
            vehicle_data.get("parking_spot_no"),
            vehicle_data.get("description"),
            vehicle_data.get("user_id")
        )
    }
    return out, 201

@app.route("/vehicles/<int:pk>", methods=["PUT"]) # pk stands for Primary Key
def update_vehicle(pk):
    out = {
        "ok": True,
        "message": "Success"
    }
    vehicle.update(pk)
    return out, 200

@app.route("/vehicles/<int:pk>", methods=["GET"])
def get_single_vehicle(pk):
    out = {
        "ok": True,
        "message": "Success",
        "body": vehicle.select(pk)
    }
    return out, 200

@app.route("/users/<int:pk>/vehicles", methods=["GET"])
def get_vehicles_for_user(pk):
    out = {
        "ok": True,
        "message": "Success",
        "body": vehicle.select_by_user_id(pk)
    }
    return out, 200