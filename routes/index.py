from . import routes


@routes.route("/")
def index():
    return "Hello from the new run method"
