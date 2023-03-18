from .settings import server

@server.route("/members")
def test_members():
    return {
        "members": ["M1", "M2", "M3", "M4"]
    }
