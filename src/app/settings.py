import os
import logging
import dotenv

_logger = logging.Logger(__file__)


class Configs:

    def __init__(self):
        if os.path.isfile('.env'):
            _logger.info('Loading .env file ...')
            dotenv.load_dotenv()

        self.APP_HOST = os.getenv('APP_HOST', '0.0.0.0')
        self.APP_PORT = int(os.getenv('APP_PORT', '8080'))
        self.APP_RELOAD = bool(os.getenv('APP_RELOAD', 'True'))

        self.API_TITLE = os.getenv('API_TITLE', 'Sample API')
        self.API_VERSION = os.getenv('API_VERSION', '1.0')
        self.API_DESCRIPTION = os.getenv(
            'API_DESCRIPTION',
            'Sample API Server to demonstrate how simple is to build one API server with FastAPI'
        )
        self.API_WELCOME_MESSAGE = os.getenv('API_WELCOME_MESSAGE', 'Welcome to Demo API Server')

        self.DB_NAME = os.getenv('DB_NAME', 'commentsdb')
        self.DB_HOST = os.getenv('DB_HOST', 'localhost:27017')
        self.DB_USERNAME = os.getenv('DB_USERNAME', 'admin')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')

configs = Configs()
