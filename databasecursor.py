class DatabaseCursor:

    def __init__(self, database):
        self.database = database
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = self.database.connection()
        self.cursor = self.connection.cursor
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()
