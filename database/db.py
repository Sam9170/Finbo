from pymongo import MongoClient
import os

# Function to create a connection to MongoDB
def create_connection():
    try:
        # Connect to the local MongoDB instance (default host and port)
        client = MongoClient(os.getenv("Mongo_DB_URL"))
        print("Connection to MongoDB successful!")
        return client
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Create a connection
client = create_connection()



