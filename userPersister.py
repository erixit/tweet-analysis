from databasecursor import DatabaseCursor
from user import User


class UserPersister:

    def __init__(self, database):
        self.database = database

    def save_to_db(self, user):
        with self.database.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    insert into 
                    users(email, first_name, last_name) 
                    values (%s, %s, %s)
                    """,
                               (user.email, user.first_name, user.last_name))

    def load_from_db_using_email(self, email):
        with self.database.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                            select first_name, last_name, id 
                              from users
                             where email = %s
                            """,
                               (email,))
                row = cursor.fetchone()
                if row:
                    return User(email, row[0], row[1], row[2])


