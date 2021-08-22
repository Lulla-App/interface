from flask import redirect
from api_integrations import microsoft_authorization_uri
from . import routes


@routes.route("/microsoft_authorize")
def microsoft_authorize():
    return redirect(microsoft_authorization_uri)
