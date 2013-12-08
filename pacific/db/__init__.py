"""
This package provides an API for relational databases.
"""
import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker

from pacific.db.repository import repository_config
from pacific.db.repository import add_repository
from pacific.db.repository import RequestRepository


__all__ = ['repository_config']


# SQLAlchemy database engines & sessions. Updated by includeme().
SESSION_FACTORIES = {}


def includeme(config):
    """ Pyramid configuration entry point.
    Call me before using any of the SQL Sessions.

    :param config: Pyramid configurator instance
    :type config: :class:`pyramid.config.Configurator`
    """
    global SESSION_FACTORIES

    options_prefix = 'pacific.db.'

    for key, value in config.registry.settings.items():
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

        shard_sessions = SESSION_FACTORIES.setdefault(domain, {})
        shard_sessions[shard] = sessionmaker(bind=engine, autocommit=False)

    config.add_request_method(request_db, 'db', reify=True)
    config.add_request_method(request_repository, 'repository', reify=True)
    # Add a directive that is capable of registering project repositories
    config.add_directive('add_repository', add_repository)


def request_db(request):
    request.add_finished_callback(lambda request: request.db.discard())
    return RequestDB()


def request_repository(request):
    return RequestRepository


class RequestDB(object):
    def __init__(self):
        self.sessions = {}

    def get_connection(self, namespace, shard='default'):
        """
        Returns a SQLAlchemy Session object according to given namespace and shard.

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
            session = SESSION_FACTORIES[namespace][shard]()
            self.sessions[key] = session
            return session

    def discard(self):
        for sess in self.sessions.values():
            sess.close()
