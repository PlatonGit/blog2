import pymysql # ignore that


class DbService:
    instance = None 
    connection = None
    cursor = None


    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            cls.connection = pymysql.connect(
                host='127.0.0.1',
                user='my_user',
                password='3212#Moya3212',
                db='blog_hw',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            cls.cursor = cls.connection.cursor()
        return cls.instance


    def execute(self, query):
        """
        Returns the description of the query and of the exception, if there is one.
        :param query: - str, for requests to the database.
        :return str: - description of the request's result.
        """
        self.cursor.execute(query)
        self.connection.commit()

        return self.cursor.description


    def close(self):
        """
        Closes all of the connections with the database
        """
        if self.cursor is not None:
            self.cursor.close()

        if self.connection is not None:
            self.connection.close()


if __name__ == '__main__':
    print('Launching this file directly isn\'t recommended. Debugging stopped.')



