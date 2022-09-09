def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://dev-morgan-admin:oxsuiNupoeJEqED1@cluster0.gurz1.mongodb.net/test"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['to_do_list']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    collection_name = dbname["friday"]
    morning = {
        "8am" : "WAKE UP",
        "9am" : "(wake up)",
        "10am" : "GRAB A BRUSH AND PUT A LITTLE MAKE-UP"
        }
    afternoon = {
        "12pm" : "go back to sleep"
        }
    collection_name.insert_many([morning, afternoon])
        
