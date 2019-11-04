from decouple import config
from dotenv import load_dotenv

load_dotenv()


HOST = config('HOST', default='0.0.0.0')
PORT = config('PORT', default=8000, cast=int)
DEBUG = config('DEBUG', default=False, cast=bool)
ACCESS_LOG = config('ACCESS_LOG', default=False, cast=bool)
