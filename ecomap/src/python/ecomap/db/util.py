from ecomap.dbpool import db_pool, retry
import logging
log = logging.getLogger('util')


@retry
def create_user(json):
    with db_pool().manager() as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO user (first_name, last_name, email, password)'
            'VALUES ("%s", "%s", "%s", "%s");' % (json['first_name'], json['last_name'], json['email'], json['password']))
        conn.commit()
