from db import DbService
from models import User
from custom_exceptions import RepositoryError
from models import Profile
from models.controllers import ProfileController
import models.repositories


class UserRepository:
    __db = None

    def __init__(self, db: DbService):
        self.__db = db
        

    def create_user(self, user: User):
        """
        Serves as a creator of users in the database.
        :param user: - User.
        """
        
        try:
            query = "INSERT INTO blog_user (username, password, profile_id) VALUES ('{username}', '{password}', {profile_id})"
            query = query.format(
                username = user.username,
                password = user.password,
                profile_id = user.profile_id
            )
            self.__db.execute(query)

        except Exception as ex:
            print(ex)
            raise RepositoryError


    def select_user(self, id):
        """
        Returns User's instance from database with corresponding id.
        :param id: - int.
        :return User: - successful select means that there is a record with corresponding id.
        :raise RepositoryError: - error occured while working with database.
        """
        
        try:
            query = "SELECT * FROM blog_user WHERE id = %d" % id
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                return User.from_dict(self.__db.cursor.fetchone())
            else:
                return None

        except Exception as ex:
            print(ex)
            raise RepositoryError


    def select_user_login_info(self, username, password):
        """
        Returns an instance of a class User, if there is corresponding data in the database
        :param username: - str
        :param password: - str
        :return (User, Profile): - successful read of the data required
        :return (None, None): - incorect data / required data doesn't exist in the database
        :raise RepositoryError: - error occured while working with the database
        """

        try:
            query = "SELECT * FROM blog_user WHERE username = '{username}' AND password = '{password}'"
            query = query.format(username = username, password = password)
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                user = User.from_dict(self.__db.cursor.fetchone())
                
                if user:
                    profile_repo = models.repositories.ProfileRepository(self.__db)
                    profile_controller = ProfileController(profile_repo)
                    profile = profile_controller.read_profile(user.profile_id)

                    if profile:
                        return (user, profile)
            elif self.__db.cursor.rowcount > 1:
                raise RepositoryError
            
            return (None, None)
        except Exception as ex:
            print(ex)
            raise RepositoryError
            

    def update_user(self, user: User):
        """
        Updates User's instance with corrsponding description and / or data.
        :param user: - User
        :raise RepositoryError: - error occured while working with database.
        """

        try:
            query = "UPDATE blog_user SET username = '{username}', password = '{password}', profile_id = {profile_id} WHERE id = {id}"
            query = query.format(
                id = user.id,
                username = user.username,
                password = user.password,
                profile_id = user.profile_id
            )
            self.__db.execute(query)

        except Exception as ex:
            print(ex)
            raise RepositoryError


    def delete_user(self, id):
        """
        Deletes User's instance from database with corresponding id.
        :param id: - int.
        :raise RepositoryError: - error occured while working with database.
        """
        
        try:
            query = "DELETE FROM blog_user WHERE id = %d" % id
            self.__db.execute(query)

        except Exception as ex:
            print(ex)
            raise RepositoryError



    
    