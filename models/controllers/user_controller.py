from models.blog_user import User


class UserController:
    __user_repo = None

    def __init__(self, user_repo):
        self.__user_repo = user_repo


    def create_user(self, user):
        return self.__user_repo.create_user(user)


    def read_user_by_id(self, id):
        return self.__user_repo.select_user(id)


    def read_user_login_info(self, username, password):
        """
        {
            'status': 'success' / 'fail',
            'user': User / None 
        }
        """
        
        result = {}

        user, profile = self.__user_repo.select_user_login_info(username, password)
        
        result['status'] = 'fail' if user is None or profile is None else 'success'
        result['user'] = user
        result['profile'] = profile

        return result


    def update_user(self, user: User):
        return self.__user_repo.update_user(user)
        

    def delete_user(self, id):
        return self.__user_repo.delete_user(id)