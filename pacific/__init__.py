from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    config.include('pacific.db')

    setup_apps(config)

    #config.add_static_view('static', 'static', cache_max_age=3600)
    #config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()


def setup_apps(config):
    """

    :param config:
    :type config: :class:`pyramid.config.Configurator`
    """
    apps_list = config.registry.settings['apps'].split(' ')
    apps = {}
    for app_mapping in apps_list:
        app_name, url_prefix = app_mapping.split('=>', 1)
        apps[app_name] = url_prefix
