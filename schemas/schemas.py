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


def userEntity(user) -> dict:
    return {
        "id" : str(user['_id']), 
        "username": user['username'],
        "password": user['password'], 
        "email": user['email']
    }

def usersEntity(entity) -> list:
    return [userEntity(user) for user in entity]