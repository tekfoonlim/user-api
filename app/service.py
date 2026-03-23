import uuid
from app import repository

def get_users(search=None, sort="name", order="asc"):
    users = repository.get_all_users()

    # Search
    if search:
        search = search.lower()
        users = [
            u for u in users
            if search in u["name"].lower() or search in u["email"].lower()
        ]

    # Sort
    if sort in ["name", "email"]:
        if order.upper() not in ["ASC","DESC"]:
            return {
            "message": "Invalid Sorting Order. Valid sorting orders are either 'asc' or 'desc'."
            }
        users.sort(
            key=lambda x: x[sort].lower(),
            reverse=(order.lower() == "desc")
        )
    else:
        return {
            "message": "Invalid Sorting Value. Valid values are either 'name' or 'email'."
        }

    return users

def get_user(user_id):
    user = repository.get_user_by_id(user_id)
    if not user:
        raise Exception("User not found")
    return user

def create_user(data):
    user = {
        "id": str(uuid.uuid4()),
        "name": data.name,
        "email": data.email
    }
    return repository.create_user(user)

def update_user(user_id, data):
    existing = repository.get_user_by_id(user_id)
    if not existing:
        raise Exception("User not found")

    updated = existing.copy()

    if data.name is not None:
        updated["name"] = data.name
    if data.email is not None:
        updated["email"] = data.email

    return repository.update_user(user_id, updated)

def delete_user(user_id):
    existing = repository.get_user_by_id(user_id)
    if not existing:
        raise Exception("User not found")

    deleted_user_details = repository.delete_user(user_id)
    #Returns details of Deleted User
    return existing