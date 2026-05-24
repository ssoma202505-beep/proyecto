from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

print("HOST:", os.getenv("MYSQL_HOST"))
print("USER:", os.getenv("MYSQL_USER"))