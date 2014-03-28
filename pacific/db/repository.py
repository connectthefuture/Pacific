import venusian


class repository_config(object):
    venusian = venusian

    def __init__(self, namespace, name, shard='default'):
        """
        :param name: unique repository name
        :type name: str
        :param namespace: namespace name according to Pacific config.
        :type namespace: str
        :param shard: one of the namespace shards. Shard 'default' is required to be set up
                      in the config.
        :type shard: str
        """
        settings = {
            'namespace': namespace,
            'name': name,
            'shard': shard
        }
        self.__dict__.update(settings)

    def __call__(self, wrapped_class):
        """

        :param wrapped_class: a class object that implements a repository
        :return: the same class object
        """
        settings = self.__dict__.copy()

        def callback(scanner, name, ob):
            scanner.config.add_repository(repository=wrapped_class, **settings)

        self.venusian.attach(wrapped_class, callback, category='pacific')
        return wrapped_class


def add_repository(config, repository, namespace, name, shard, **kw):
    """ This function is used as a directive of Pyramid Config
    and responsible for registering available SQL repositories.

    :param config: Pyramid configurator instance
    :type config: :class:`pyramid.config.Configurator`
    :param repository: repository class object
    :param namespace: database namespace
    :type namespace: str
    :param name: database name, must be unique
    :type name: str
    :param shard: database shard
    :type shard: str
    """
    repositories = config.registry.settings.setdefault('pacific.db.repositories', {})
    repositories[name] = {
        'repository': repository,
        'namespace': namespace,
        'shard': shard
    }


class RequestRepositories(object):
    """ Instances of this class will be attached to each request as ``request.db.repositories``
    """
    def __init__(self, request):
        """
        :type request: :class:`pyramid.request.Request`
        """
        self.request = request
        self.repositories = request.registry.settings['pacific.db.repositories']
        self.instances = {}

    def get(self, name):
        """

        :param name: repository name
        :type name: str
        :return: repository instance

        """
        try:
            return self.instances[name]
        except KeyError:
            credentials = self.repositories[name]
            db_session = self.request.db.get_connection(credentials['namespace'], credentials['shard'])
            instance = credentials['repository'](db_session)
            self.instances[name] = instance
            return instance
