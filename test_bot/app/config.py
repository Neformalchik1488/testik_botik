import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")

REDIS_HOST=os.environ.get("REDIS_HOST")
REDIS_PORT = int(os.environ.get("REDIS_PORT"))
REDIS_DB = os.environ.get("REDIS_DB")

PSQL_USER = os.environ.get("PSQL_USER")
PSQL_PASS = os.environ.get("PSQL_PASS")
PSQL_HOST = os.environ.get("PSQL_HOST")
PSQL_PORT = int(os.environ.get("PSQL_PORT"))
PSQL_NAME = os.environ.get("PSQL_NAME")