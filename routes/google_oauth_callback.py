from flask import request, jsonify
from urllib.parse import urlparse
from . import routes
from api_integrations import get_oauth_token_from_google
from data_access import add_google_oauth_tokens_to_database
from glue import GoogleScope, GoogleScopeMap, GoogleScopeURI


@routes.route("/google_callback")
def google_oauth_callback():
    try:
        raw_scopes = str(request.args.get("scope"))
        scope_map = GoogleScopeMap()
        for scope in raw_scopes.split():
            divide_index = scope.rfind("/")
            scope_map.add(
                GoogleScope(scope[divide_index + 1 :]),
                set([GoogleScopeURI(scope[: divide_index + 1])]),
            )

        oauth_token = get_oauth_token_from_google(
            str(request.args.get("code")), scope_map
        )
        add_google_oauth_tokens_to_database([oauth_token])
        # Should there be a system to log unexpected fields?
        return jsonify(message="job done")
    except Exception as e:
        raise e
