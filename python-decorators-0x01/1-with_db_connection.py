import sqlite3
import functools

def with_db_connection(func):
    """
    Decorator that opens a SQLite database connection,
    passes it to the decorated function, and closes it afterwards.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')  # open connection
        try:
            result = func(conn, *args, **kwargs)  # pass connection as first arg
        finally:
            conn.close()  # ensure connection is closed
        return result
    return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    """
    Fetch a user by ID using the passed database connection.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return user


# Example usage
if __name__ == "__main__":
    user = get_user_by_id(user_id=1)
    print(user)
