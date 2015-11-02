from pyramid.config import Configurator
import cliquet
from cliquet.authorization import RouteFactory


def includeme(config):
    config.scan("cliquet.tests.testapp.views")


def main(settings=None, config=None, *args, **additional_settings):
    if settings is None:
        settings = {}
    settings.update(additional_settings)
    if config is None:
        config = Configurator(settings=settings, root_factory=RouteFactory)
    cliquet.initialize(config, version='0.0.1')
    config.include(includeme)
    app = config.make_wsgi_app()
    # Install middleware (idempotent if disabled)
    return cliquet.install_middlewares(app, settings)
