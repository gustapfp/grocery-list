def itemEntity(item) -> dict:
    return {
        "id" : str(item["_id"]),
        "name" : item['name'],
        "price": item['price'],
        "description": item["description"],
        "store" : item["store"]
    }
    
def itemsEntity(entity) -> list:
    return [itemEntity(item) for item in entity]
