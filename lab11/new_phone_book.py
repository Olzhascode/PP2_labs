import psycopg2
import re

conn = psycopg2.connect(
    dbname="newphonebook",
    user="postgres",
    password="Kesha2412:)",
    host="localhost",
    port="5432"
)
conn.autocommit = True


def search_users(pattern):
    like_pattern = f"%{pattern}%"
    result = []

    try:
        cursor = conn.cursor()
        query = """
            SELECT * FROM users
            WHERE name ILIKE %s OR surname ILIKE %s OR phone ILIKE %s;
        """
        cursor.execute(query, (like_pattern, like_pattern, like_pattern))
        result = cursor.fetchall()
    except Exception as e:
        print("Error while searching for users:", e)
    finally:
        if 'cursor' in locals():
            cursor.close()

    return result


def insert_or_update_user(name, surname, phone):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM users WHERE name = %s AND surname = %s;", (name, surname))
        if cursor.fetchone():
            
            cursor.execute(
                "UPDATE users SET phone = %s WHERE name = %s AND surname = %s;",
                (phone, name, surname)
            )
        else:
            cursor.execute(
                "INSERT INTO users (name, surname, phone) VALUES (%s, %s, %s);",
                (name, surname, phone)
            )

    except Exception as e:
        print(f"Error while inserting/updating user {name} {surname}:", e)
    finally:
        if 'cursor' in locals():
            cursor.close()


def insert_many_users(user_list):
    invalid = []

    for name, surname, phone in user_list:
        if re.fullmatch(r"\d{10,15}", phone):
            try:
                insert_or_update_user(name, surname, phone)
            except Exception as e:
                print(f"Error while inserting user {name} {surname} with phone {phone}:", e)
                invalid.append((name, surname, phone))
        else:
            invalid.append((name, surname, phone))

    return invalid


def get_users_paginated(limit, offset):
    result = []
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM users ORDER BY id
            LIMIT %s OFFSET %s;
        """, (limit, offset))
        result = cursor.fetchall()
    except Exception as e:
        print("Error while retrieving users with pagination:", e)
    finally:
        if 'cursor' in locals():
            cursor.close()

    return result


def delete_user(identifier):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM users
            WHERE name = %s OR surname = %s OR phone = %s;
        """, (identifier, identifier, identifier))
    except Exception as e:
        print(f"Error while deleting user with identifier {identifier}:", e)
    finally:
        if 'cursor' in locals():
            cursor.close()


if __name__ == "__main__":
    try:
        pass
        
    finally:
        conn.close()
