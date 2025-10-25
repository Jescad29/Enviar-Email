from dotenv import load_dotenv
import os

load_dotenv()

api_myemail = os.getenv("MYEMAIL")
api_key = os. getenv("PASSWORD")


print("Api_key= ", api_key)
print("Api_myemail= ", api_myemail)
