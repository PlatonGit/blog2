from db import DbService
from models import Profile
from custom_exceptions import RepositoryError


class ProfileRepository:
    __db = None

    def __init__(self, db: DbService):
        self.__db = db

    
    def create_profile(self, profile: Profile):
        """
        Serves as a creator of profiles in the database.
        :param profile: - Profile.
        :raise RepositoryError: - error occured while working with database.
        """
        try:
            query = "INSERT INTO profile (first_name, second_name, last_name, age) VALUES ('{first_name}', '{second_name}', '{last_name}', {age})"
            query = query.format(
                first_name = profile.first_name,
                second_name = profile.second_name,
                last_name = profile.last_name,
                age = profile.age
            )
            self.__db.execute(query)

        except Exception as error:
            print(f'\n>>> Error: {error} <<<')
            raise RepositoryError

    
    def create_blank_profile(self):
        """
        Creates an empty profile and returns it's id.
        """

        try:
            # creating a blank profile
            query = "INSERT INTO profile () VALUES ();"
            self.__db.execute(query)

            # getting it's id
            query = "SELECT max(id) as id FROM profile;"
            self.__db.execute(query)
            
            # returning the id if one was found
            if self.__db.cursor.rowcount == 1:
                return self.__db.cursor.fetchone()['id']
            else:
                return None
      
        except Exception as error:
            print(f'\n>>> Error: {error} <<<')
            raise RepositoryError


    def select_profile(self, id):
        """
        Returns Profile's instance from database with corresponding id.
        :param id: - int.
        :return User: - successful selection means that there is a record with corresponding id.
        :raise RepositoryError: - error occured while working with database.
        """
        
        try:
            query = "SELECT * FROM profile WHERE id = %d" % id                          
            self.__db.execute(query) 
                     
            if self.__db.cursor.rowcount == 1:
                return Profile.from_dict(self.__db.cursor.fetchone())
            else:
                return None

        except Exception as error:
            print(f'\n>>> Error: {error} <<<')
            raise RepositoryError


    def update_profile(self, profile: Profile):
        """
        Updates Profile's instance with corrsponding description and / or data.
        :param profile: - Profile
        :raise RepositoryError: - error occured while working with database.
        """

        try:
            query = "UPDATE profile SET first_name = '{first_name}', second_name = '{second_name}', last_name = '{last_name}', age = {age} WHERE id = {id}"
            query = query.format(
                id = profile.id,
                first_name = profile.first_name,
                second_name = profile.second_name,
                last_name = profile.last_name,
                age = profile.age if profile.age is not None else 'NULL'
            )
            
            self.__db.execute(query)
            
            return True

        except Exception as error:
            print(f'\n>>> Error: {error} <<<')
            raise RepositoryError


    def delete_profile(self, id):
        """
        Deletes Profile's instance from database with corresponding id.
        :param id: - int.
        :raise RepositoryError: - error occured while working with database.
        """
        
        try:
            query = "DELETE FROM profile WHERE id = %d" % id
            self.__db.execute(query)

        except Exception as error:
            print(f'\n>>> Error: {error} <<<')
            raise RepositoryError

