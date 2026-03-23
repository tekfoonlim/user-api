from fastapi import APIRouter, HTTPException, Query
from app import service
from app.schemas import UserCreate, UserUpdate

router = APIRouter()

@router.get("/users")
def get_users(
    search: str = Query(None),
    sort: str = Query("name"),
    order: str = Query("asc")
):
    return service.get_users(search, sort, order)

@router.get("/users/{user_id}")
def get_user(user_id: str):
    try:
        return service.get_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/users", status_code=201)
def create_user(user: UserCreate):
    return service.create_user(user)

@router.put("/users/{user_id}")
def update_user(user_id: str, user: UserUpdate):
    try:
        return service.update_user(user_id, user)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    try:
        deleted_user = service.delete_user(user_id)
        return {
            "message": "User deleted successfully",
            "data": deleted_user
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))