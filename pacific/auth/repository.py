from pacific.db import repository_config


@repository_config(namespace='pacific', name='users')
class UsersRepository(object):
    def __init__(self, db_session):
        """

        :param db_session: SQLAlchemy's Session instance.
        :type db_session: :class:`sqlalchemy.orm.session.Session`
        """
        self.db = db_session

    def get_by_id(self, user_id):
        """

        :param user_id:
        :type user_id: int
        """
        return self.db.execute("SELECT 1").fetchone()
