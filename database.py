from psycopg import _connection_info
from psycopg_pool import ConnectionPool
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)
logging.getLogger("psycopg.pool").setLevel(logging.INFO)


class Database:

    def __init__(self, **kwargs):
        connection_info = _connection_info.make_conninfo('', **kwargs)
        self.connection_pool = ConnectionPool(connection_info,min_size=1, max_size=1, timeout=10)

    def connection(self):
        return self.connection_pool.connection()

    def close(self):
        self.connection_pool.close()
