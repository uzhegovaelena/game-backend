from handlers import play_game


def setup_routes(app):
    app.router.add_post("/games", play_game)
