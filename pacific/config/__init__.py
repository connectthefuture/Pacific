""" Pacific Config utilities
"""

def parse_db_settings(db):
    rv = {}
    for cluster in db:
        for db_name, credentials in db[cluster].items():
            item = 'pacific.db.{}.{}'.format(cluster, db_name)
            rv[item] = 'postgresql+psycopg2://{user}:{password}@:{port}/{database}?host={host}'.format(**credentials)
    return rv
