from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env', override=True)

#^ Load the .env file
SECRET_KEY=os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'


#^ Import WSGI request handler
from django.core.handlers.wsgi import WSGIRequest as Request
