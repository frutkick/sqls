from ecomap.dbpool import db_pool, retry
import logging

log = logging.getLogger('retry')


@retry
def create_user(json):
    with db_pool().manager() as conn:
        cur = conn.cursor()
        sql = """INSERT INTO `user` (`first_name`, `last_name`, `email`, `password`)
                 VALUES ("%s", "%s", "%s", "%s");""" % (json['first_name'],
                                                        json['last_name'],
                                                        json['email'],
                                                        json['password'])
        cur.execute(sql)
        conn.commit()
        log.info('Created user.')


@retry
def login(json):
    response = {}
    with db_pool().manager() as conn:
        cur = conn.cursor()
        sql = """SELECT `first_name`, `last_name`, `email`, `password` FROM `user`
        WHERE email="%s";""" % (json['email'])
        cur.execute(sql)
        result = cur.fetchone()
        log.info('Got: %s.', result)
        response['first_name'] = result[0]
        response['last_name'] = result[1]
        response['email'] = result[2]
        response['password'] = result[3]
    return response
