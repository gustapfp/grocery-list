from fastapi import APIRouter, status, HTTPException
from config.db import DB_grocery
from models.item import Item
from schemas.schemas import itemEntity, itemsEntity
from bson import ObjectId


item = APIRouter(
    tags=['Items'], 
    prefix='/items'
   
)

@item.post("/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    """_summary_
    Create a Item for the grocery list

    Args:
        item (Item): Item from the list

    Returns:
        dict: json response with the item created
    """
    new_item = DB_grocery.item.insert_one(dict(item))
    return itemEntity(DB_grocery.item.find_one({"_id": new_item.inserted_id}))
    
@item.get('/', status_code=status.HTTP_200_OK)
async def get_all_items():
    """
    Get all items from the list
    Returns:
        _type_: list of items 
    """
    items = list(DB_grocery.item.find())
    if len(items) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This list is empity! Try add some items in the list.")
    return itemsEntity(DB_grocery.item.find())

@item.get('/{id}', status_code=status.HTTP_200_OK)
async def get_item(id):
    """
    Return a specific item from the list

    Returns:
        _type_: _description_
    """
    selected_item = DB_grocery.item.find_one({'_id': ObjectId(id)})
    
    if not selected_item:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The list elemento of id: {id}, doesn't exist!") 
    return itemEntity(selected_item)

@item.put('/{id}', status_code=status.HTTP_200_OK)
async def update_item(id, item: Item):
    """Update a specific item from the grocery list

    Args:
        id (_type_): _description_
        item (Item): _description_

    Returns:
        _type_: _description_
    """
    DB_grocery.item.find_one_and_update(
        {'_id': ObjectId(id)},{
        '$set':dict(item)
        }
    )
    return itemEntity(DB_grocery.item.find_one({'_id': ObjectId(id)}))

@item.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(id, item:Item):
    """Delete a specific a item from the grocery list
    """
    return itemEntity(DB_grocery.item.find_one_and_delete({'_id': ObjectId(id)}))