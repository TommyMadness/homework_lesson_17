# GET /users/2
user_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string", "format": "email"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string"},
            },
            "required": ["id", "email", "first_name", "last_name", "avatar"],
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "text": {"type": "string"},
            },
            "required": ["url", "text"],
        },
    },
    "required": ["data", "support"],
}

# POST /register
register_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "token": {"type": "string"},
    },
    "required": ["id", "token"],
}

# POST /users
create_user_response_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
    },
    "required": ["name", "job", "id", "createdAt"],
}

# PUT /users/2
update_user_response_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"},
    },
    "required": ["name", "job", "updatedAt"],
}
