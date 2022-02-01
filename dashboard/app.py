
from flakon import create_app as _create
from .views import blueprints


def create_app(settings=None):
    app = _create(blueprints=blueprints, settings=settings)
    return app
