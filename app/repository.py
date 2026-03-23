import json
import os

FILE_PATH = "data/users.json"

def read_users():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def write_users(users):
    with open(FILE_PATH, "w") as f:
        json.dump(users, f, indent=2)

def get_all_users():
    return read_users()

def get_user_by_id(user_id):
    users = read_users()
    return next((u for u in users if u["id"] == user_id), None)

def create_user(user):
    users = read_users()
    users.append(user)
    write_users(users)
    return user

def update_user(user_id, updated_user):
    users = read_users()
    new_users = []

    for u in users:
        if u["id"] == user_id:
            new_users.append(updated_user)
        else:
            new_users.append(u)

    write_users(new_users)
    return updated_user

def delete_user(user_id):
    users = read_users()
    users = [u for u in users if u["id"] != user_id]
    write_users(users)
    deleted_user_details = [u for u in users if u["id"] == user_id]
    return deleted_user_details