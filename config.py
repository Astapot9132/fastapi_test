import os
import dotenv

dotenv.load_dotenv()


YANDEX_TOKEN = os.getenv('YANDEX_TOKEN')
POSTGRES_LOGIN = os.getenv('POSTGRES_LOGIN')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_NAME = os.getenv('POSTGRES_NAME')

print(YANDEX_TOKEN)
print(POSTGRES_LOGIN)
print(POSTGRES_PASSWORD)
print(POSTGRES_HOST)
print(POSTGRES_NAME)