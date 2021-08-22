from flask import Blueprint

routes = Blueprint("routes", __name__)

from .index import index
from .microsoft_oauth_callback import microsoft_oauth_callback
from .microsoft_authorize import microsoft_authorize
