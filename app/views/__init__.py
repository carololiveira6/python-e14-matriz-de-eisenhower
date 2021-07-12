from flask import Flask


def init_app(app: Flask):
    from .categories_views import bp as bp_category
    from .tasks_view import bp as bp_tasks
    from .tasks_categories_view import bp as bp_tasks_categories
    from .all_data_views import bp as bp_all_data

    app.register_blueprint(bp_category)
    app.register_blueprint(bp_tasks)
    app.register_blueprint(bp_tasks_categories)
    app.register_blueprint(bp_all_data)
