from flask import Flask
import json
from routes import routes

app = Flask(__name__)

app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", ssl_context="adhoc")
