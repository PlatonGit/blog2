class User:
    __slots__ = ('id', 'created_at', 'username', 'password', 'profile_id')

    def __init__(
        self,
        username,
        password,
        profile_id,
        id = None,
        created_at = None
    ):
        self.id = id
        self.created_at = created_at
        self.username = username
        self.password = password
        self.profile_id = profile_id


    @classmethod
    def from_dict(cls, data):
        return User(**data)