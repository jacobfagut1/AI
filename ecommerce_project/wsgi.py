import os
import logging
from django.core.wsgi import get_wsgi_application

# Set up logging to check for issues
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Log the environment variables for debugging
logger.debug("DJANGO_SETTINGS_MODULE: %s", os.getenv('DJANGO_SETTINGS_MODULE'))
logger.debug("PORT: %s", os.getenv('PORT'))

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')

# Initialize the WSGI application
application = get_wsgi_application()
