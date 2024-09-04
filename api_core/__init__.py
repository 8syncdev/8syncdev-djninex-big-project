from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env', override=True)

#^ Load the .env file
SECRET_KEY=os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'
FRONT_END_URL = ['http://localhost:3000'] if DEBUG else os.getenv('FRONT_END_URL').split('|')[1:] #* 1st is localhost, 2nd > is production


#^ Import WSGI request handler
from django.core.handlers.wsgi import WSGIRequest as Request
