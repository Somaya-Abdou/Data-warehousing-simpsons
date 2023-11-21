import psycopg2
import configparser 
import redshift_sql

def drop_tables (cur,drop_tables):
    for table in drop_tables :
        cur.execute(table)

def create_tables (cur,create_tables):
    for table in create_tables :
        cur.execute(table)

def insert_into_tables (cur,insert_into_tables):
    for table in insert_into_tables :
        cur.execute(table)

def move_to_s3 (cur,tables,s3_url,key,secret,iam_role_name,region) :
    for table in tables :
        cur.execute("""UNLOAD ('SELECT * FROM {}') TO '{}'
                     credentials 'aws_iam_role={}'
                     parallel off delimiter ','  gzip  region '{}';
                     """.format(table,s3_url,iam_role_name,region))


def main():
    config = configparser.ConfigParser()
    config.read('redshiftlogin.cfg')
    host = config.get('RedShift', 'host')
    dbname = config.get('RedShift','dbname')
    user = config.get('RedShift', 'user')
    password = config.get('RedShift','password')
    port = config.get('RedShift','port')
    key = config.get('Credentials','key')
    secret = config.get('Credentials','secret')
    region = config.get('Credentials','region')
    iam_role_name = config.get('Credentials','iam_role_name')
    s3_url = config.get('Credentials','s3_url')

    conn = psycopg2.connect(host=host , dbname=dbname , user=user , password = password , port=port)
    cur = conn.cursor()
    conn.set_session(autocommit=True)
    
    drop_tables (cur,redshift_sql.drop_tables)
    create_tables (cur,redshift_sql.create_tables)
    insert_into_tables (cur,redshift_sql.insert_into_tables)
    move_to_s3 (cur,redshift_sql.tables,s3_url,key,secret,iam_role_name,region)

main()