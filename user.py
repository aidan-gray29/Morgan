import mysql.connector
from mysql.connector import Error

class User:

  def __init__(self, username):
    data = self.__extractData(username)

    self.username               = data[0]
    self.evolution              = data[1]
    self.last_interaction_date  = data[2]
    self.creation_date          = data[3]
    self.fav_food               = data[4]
    self.hated_food             = data[5]
    self.persistent_sentiment   = data[6]
    self.hunger                 = data[7]
    self.playfulness            = data[8]
    self.interactions_counter   = data[9]


  def __create_server_connection(self, host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


  def __create_db_connection(self, host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


  def __execute_query(self, connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


  def __read_query(self, connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


  def __extractData(self, username) -> tuple:
    connection    = self.__create_db_connection("hostname", "username", "pw", "bitberg_database")

  ## Returns anything if it exists
    query_exists  =  """SELECT username FROM user_states WHERE EXISTS(SELECT username FROM user_states WHERE username='{}');""".format(username)

  ## Extracts profile data from existing row
    if self.__read_query(connection, query_exists):
      return self.__extractProfile(connection, username)
 
  ## Creates profile data and extracts it
    query_insert    = """ INSERT INTO user_states(username) VALUES('{}');""".format(username)
    self.__execute_query(connection, query_insert)
    return self.__extractProfile(connection, username)
  

  def __extractProfile(self, connection, username) -> tuple:
    query_data    = """SELECT * FROM user_states WHERE username = '{}';""".format(username)
    results = self.__read_query(connection, query_data)
    print(results[0])
    return results[0]


  def close(self):
    connection    = self.__create_db_connection("hostname", "username", "pw", "bitberg_database")

    query_update = """UPDATE user_states SET evolution = {}, last_interaction = CURRENT_DATE, fav_food = '{}', hated_food = '{}', persistent_sentiment = {}, hunger = {}, playfulness = {}, interactions_counter = {}  WHERE username = '{}'""".format(self.evolution, self.fav_food, self.hated_food, self.persistent_sentiment, self.hunger, self.playfulness, self.interactions_counter, self.username)

    self.__execute_query(connection, query_update)

    self.__extractProfile(connection, self.username)
#