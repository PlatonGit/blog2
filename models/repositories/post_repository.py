from db import DbService
from models import Post
from custom_exceptions import RepositoryError


class PostRepository:
    __db = None

    def __init__(self, db: DbService):
        self.__db = db
        

    def create_post(self, post: Post):
        """
        Serves as a creator of posts in the database.
        :param post: - Post.
        :return bool: - False means error, True means successful creation.
        """
        try:
            query = "INSERT INTO post (user_id, title, text) VALUES ({user_id}, '{title}', '{text}')"
            query = query.format(
                user_id = post.user_id,
                title = post.title,
                text = post.text
            )
            self.__db.execute(query)
            
        except Exception as ex:
            print(ex)
            raise RepositoryError

    
    def select_post(self, id):
        """
        Returns Post's instance from database with corresponding id.
        :param id: - int.
        :return Post: - successful select means that there is a record with corresponding id.
        :raise RepositoryError: - error occured while working with database.
        """
        
        try:
            query = "SELECT * FROM post WHERE id = %d" % id
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                return Post.from_dict(self.__db.cursor.fetchone())
            else:
                return None

        except Exception as ex:
            print(ex)
            raise RepositoryError


    def update_post(self, post: Post):
        """
        Updates Post's instance with corrsponding description and / or data.
        :param post: - Post
        :raise RepositoryError: - error occured while working with database.
        """

        try:
            query = "UPDATE post SET user_id = {user_id}, title = '{title}', text = '{text}' WHERE id = {id}"
            query = query.format(
                id = post.id,
                user_id = post.user_id,
                title = post.title,
                text = post.text
            )
            self.__db.execute(query)

        except Exception as ex:
            print(ex)
            raise RepositoryError


    def delete_post(self, id):
        """
        Deletes Post's instance from database with corresponding id.
        :param id: - int.
        :raise RepositoryError: - error occured while working with database.
        """
        
        try:
            query = "DELETE FROM post WHERE id = %d" % id
            self.__db.execute(query)

        except Exception as ex:
            print(ex)
            raise RepositoryError


    