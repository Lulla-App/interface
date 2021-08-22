from flask import request, jsonify
from . import routes
from api_integrations import get_oauth_token_from_microsoft
from data_access import add_oauth_tokens_to_database


@routes.route("/microsoft_callback")
def microsoft_oauth_callback():
    try:
        response = get_oauth_token_from_microsoft(str(request.args.get("code")))
        # add_oauth_tokens_to_database(
        #     [
        #         {
        #             "access_token": access_token,
        #             "refresh_token": refresh_token,
        #             "source_name": "Microsoft To do",
        #         }
        #     ]
        # )

        return jsonify(**response)
    except Exception as e:
        raise e
