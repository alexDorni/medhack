from .settings import server

@server.route("/test")
def test():
    return {
        "test": "working"
    }
