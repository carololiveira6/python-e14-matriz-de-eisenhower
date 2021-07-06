from flask import Flask


def init_app(app: Flask):
    from .categories_views import bp as bp_category

    app.register_blueprint(bp_category)
