from fastapi import APIRouter, status, HTTPException
from models.user import User
from config.db import DB_grocery
from schemas.schemas import userEntity, usersEntity
from bson import ObjectId

user = APIRouter(
    prefix="/users",
    tags=['Users']
)

@user.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    """Create a User"""
    user_created = DB_grocery.user.insert_one(dict(user))
    return userEntity(DB_grocery.user.find_one({"_id" : user_created.inserted_id}))

@user.get('/', status_code=status.HTTP_200_OK)
async def get_all_users():
    """Get all users registred on the database

    Args:
        user (User): user model

    Returns:
        _type_: _description_
    """
    users = list(DB_grocery.user.find())
    if len(users) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You system doesn't have any user registred.")
    return usersEntity(DB_grocery.user.find())

@user.get('/{id}', status_code=status.HTTP_200_OK)
async def get_user(id):
    selected_user = DB_grocery.user.find_one({"_id": ObjectId(id)})
    if not selected_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The user if the id: {id} doesn't exist.")
    return userEntity(selected_user)

@user.put('/{id}', status_code=status.HTTP_200_OK)
async def update_user(id, user: User):
    selected_user = DB_grocery.user.find_one({"_id": ObjectId(id)})
    if not selected_user:      
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The user if the id: {id} doesn't exist.")
    DB_grocery.user.find_one_and_update(
        {'_id': ObjectId(id)}, 
        {'$set': dict(user)}
    )
    return userEntity(DB_grocery.user.find_one({"_id": ObjectId(id)}))

@user.delete('/{id}', status_code=status.HTTP_200_OK)
async def delete_user(id):
    selected_user = DB_grocery.user.find_one({'_id': ObjectId(id)})
    if not selected_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail=f"The user if the id: {id} doesn't exist.")
    return userEntity(DB_grocery.user.find_one_and_delete({'_id': ObjectId(id)}))
    

