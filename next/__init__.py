from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from next.models import initialize_sql


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)

    config = Configurator(settings=settings)

    config.add_static_view('static', 'next:static')
    config.add_route('index', '/')

    config.add_route('create-scenario', '/scenario/new')
    config.add_route('show-scenario', '/scenario/{id}')
    config.add_route('run-scenario', '/scenario/{id}/run')
    # config.add_route('map-scenario', '/scenario/{id}/map')
    config.add_route('show-scenario-json', '/scenario/{id}/json')

    config.scan()
    return config.make_wsgi_app()
