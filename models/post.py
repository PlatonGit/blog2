class Post:
    __slots__ = (
        'id', 
        'created_at', 
        'updated_at', 
        'user_id', 
        'title', 
        'text'
    )


    def __init__(
        self,
        user_id,
        title,
        text = None,
        id = None,
        created_at = None,
        updated_at = None
    ):
        self.id = id
        self.user_id = user_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.title = title
        self.text = text

    
    @classmethod
    def from_dict(cls, data):
        return Post(**data)