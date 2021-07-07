from flask import Flask


def init_app(app: Flask):
    from .categories_views import bp as bp_category
    from .tasks_view import bp as bp_tasks

    app.register_blueprint(bp_category)
    app.register_blueprint(bp_tasks)
