""" Pacific Config utilities
"""

def parse_db_settings(db):
    """
    :param db:
    :type db: dict
    :rtype: dict
    """
    rv = {}
    for cluster in db:
        for db_name, credentials in db[cluster].items():
            item = 'pacific.db.{}.{}'.format(cluster, db_name)
            rv[item] = 'postgresql+psycopg2://{user}:{password}@:{port}/{database}?host={host}'.format(**credentials)
    return rv


def parse_apps(apps):
    """
    :param apps: a mapping of activated applications => URL prefixes
    :type apps: dict
    :rtype: str
    """
    prepared = []
    for app_name, attributes in apps.items():
        prepared.append('{}=>{}'.format(app_name, attributes['url_prefix']))
    return ' '.join(prepared)