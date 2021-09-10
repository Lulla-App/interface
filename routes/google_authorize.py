from flask import redirect
from api_integrations import google_authorization_uri
from . import routes


@routes.route("/google_authorize")
def google_authorize():
    return redirect(google_authorization_uri)
