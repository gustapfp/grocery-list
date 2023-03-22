from fastapi import APIRouter
from config.db import DB_connection, DB_grocery
from models.item import Item
from schemas.schemas import itemEntity, itemsEntity
from bson import ObjectId

item = APIRouter(
    tags=['Item'], 
    prefix='/item'
   
)

@item.post("/")
async def create_item(item: Item):
    """_summary_
    Create a Item for the grocery list

    Args:
        item (Item): Item from the list

    Returns:
        dict: json response with the item created
    """
    DB_grocery.item.insert_one(dict(item))
    return itemEntity(DB_connection.grocery.item.find())
    
@item.get('/')
async def get_all_items():
    """
    Get all items from the list
    Returns:
        _type_: list of items 
    """
    return itemsEntity(DB_grocery.item.find())

@item.get('/{id}')
async def get_item(id):
    """
    Return a specific item from the list

    Returns:
        _type_: _description_
    """
    return itemEntity(DB_grocery.item.find_one({'_id': ObjectId(id)}))

@item.put('/{id}')
async def update_item(id, item: Item):
    DB_grocery.item.find_one_and_update(
        {'_id': ObjectId(id)},{
        '$set':dict(item)
        }
    )
    return itemEntity(DB_grocery.item.find_one({'_id': ObjectId(id)}))

@item.delete("/{id}")
async def delete_item(id, item:Item):
    return itemEntity(DB_grocery.item.find_one_and_delete({'_id': ObjectId(id)}))