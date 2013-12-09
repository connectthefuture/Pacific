"""
This package provides an API for relational databases.
"""
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from pacific.db.repository import repository_config
from pacific.db.repository import add_repository
from pacific.db.repository import RequestRepositories


__all__ = ['repository_config', 'get_session_factories']


def includeme(config):
    """ Pyramid configuration entry point.
    Call me before using any of the SQL Sessions.

    :param config: Pyramid configurator instance
    :type config: :class:`pyramid.config.Configurator`
    """
    session_factories = get_session_factories(config.registry.settings)
    config.registry.settings['pacific.db.session_factories'] = session_factories

    config.add_request_method(request_db, 'db', reify=True)
    # Add a directive that is capable of registering project repositories
    config.add_directive('add_repository', add_repository)


def get_session_factories(settings, options_prefix='pacific.db.'):
    """

    :param settings:
    :type settings: dict
    :param options_prefix:
    :type options_prefix: str
    :return: dict of session factories
    :rtype: dict
    """
    session_factories = {}
    for key, value in settings.items():
        if not key.startswith(options_prefix):
            continue

        key = key.split(options_prefix)[1]
        domain, shard = key.split('.')
        url = value
        engine = sa.create_engine(url, encoding='utf-8',
                                  # -- pool options --
                                  pool_size=10,
                                  max_overflow=10,
                                  pool_timeout=10)
        shard_sessions = session_factories.setdefault(domain, {})
        shard_sessions[shard] = sessionmaker(bind=engine, autocommit=False)
    return session_factories


def request_db(request):
    """

    :param request: Pyramid Request instance
    :return: an instance of :class:`RequestDB`
    :rtype: :class:`RequestDB`
    """
    request.add_finished_callback(lambda request: request.db.discard())
    return RequestDB(request)


class RequestDB(object):
    def __init__(self, request):
        """
        :param request: Pyramid Request instance
        :type request: :class:`pyramid.request.Request`
        """
        self.sessions = {}
        self.session_factories = request.registry.settings['pacific.db.session_factories']
        self.repositories = RequestRepositories(request)

    def get_connection(self, namespace, shard='default'):
        """ Returns a SQLAlchemy Session object according to given namespace and shard.

        :param namespace: namespace name according to Pacific config.
        :type namespace: str
        :param shard: one of the namespace shards. Shard 'default' is required to be set up
                      in the config.
        :type shard: str
        :return: A SQLAlchemy Session object.
        """
        key = '{namespace}:{shard}'.format(namespace=namespace, shard=shard)
        try:
            return self.sessions[key]
        except KeyError:
            # start a new session
            session = self.session_factories[namespace][shard]()
            self.sessions[key] = session
            return session

    def discard(self):
        """Close all sessions and return connections to the pool."""
        for sess in self.sessions.values():
            sess.close()
