class PostController:
    __post_repo = None

    def __init__(self, post_repo):
        self.__post_repo = post_repo


    def create_post(self, post):
        return self.__post_repo.create_post(post)


    def read_post(self, id):
        return self.__post_repo.select_post(id)


    def update_post(self, post):
        return self.__post_repo.update_post(post)


    def delete_post(self, id):
        return self.__post_repo.delete_post(id)