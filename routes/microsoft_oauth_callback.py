from flask import request, jsonify
from . import routes
from api_integrations import get_oauth_token_from_microsoft
from data_access import add_oauth_tokens_to_database, add_microsoft_oauth_tokens_to_database
from glue import MicrosoftOAuthToken, TokenType, MicrosoftScope


@routes.route("/microsoft_callback")
def microsoft_oauth_callback():
    try:
        oauth_token = get_oauth_token_from_microsoft(str(request.args.get("code")))
        add_microsoft_oauth_tokens_to_database([oauth_token])
        print(oauth_token)
        # Should there be a system to log unexpected fields?
        return jsonify(message="job done")
    except Exception as e:
        raise e
