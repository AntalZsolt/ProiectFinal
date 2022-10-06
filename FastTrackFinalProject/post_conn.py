import psycopg2


def connection_postgres():
    try:
        return psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="GitHubAnTaL1-")
    except psycopg2.DatabaseError as error:
        print(error)



