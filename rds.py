import psycopg2
import configparser 
import pandas as pd
import rds_sql

def read_csv (path):
    df1 = pd.read_csv(path[0]) 
    df2 = pd.read_csv(path[1]) 
    df3 = pd.read_csv(path[2]) 
    df4 = pd.read_csv(path[3]) 
    df5 = pd.read_csv(path[4]) 
    df6 = pd.read_csv(path[5])
    return (df1,df2,df3,df4,df5,df6) 

def drop_tables (cur,drop_tables):
    for table in drop_tables :
        cur.execute(table)

def create_tables (cur,create_tables):
    for table in create_tables :
        cur.execute(table)

def insert_into_tables (cur,insert_into_tables,df1,df2,df3,df4,df5,df6):
    for index,row in df1.iterrows():
        cur.execute(insert_into_tables[0],row)
    for index,row in df2.iterrows():
        cur.execute(insert_into_tables[1],row) 
    for index,row in df3.iterrows():
        cur.execute(insert_into_tables[2],row)
    for index,row in df4.iterrows():
        cur.execute(insert_into_tables[3],row)
    for index,row in df5.iterrows():
        cur.execute(insert_into_tables[4],row) 
    for index,row in df6.iterrows():
        cur.execute(insert_into_tables[5],row)                  

def main():
    config = configparser.ConfigParser()
    config.read('rdslogin.cfg')
    host = config.get('DataBase', 'host')
    dbname = config.get('DataBase','dbname')
    user = config.get('DataBase', 'user')
    password = config.get('DataBase','password')
    port = config.get('DataBase','port')

    conn = psycopg2.connect(host=host , dbname=dbname , user=user , password = password , port=port)
    cur = conn.cursor()
    conn.set_session(autocommit=True)
    
    paths = ['atlas-query-simpsons-season-20\Person.csv' ,'atlas-query-simpsons-season-20\Award.csv',\
             'atlas-query-simpsons-season-20\Episode.csv', 'atlas-query-simpsons-season-20\Credit.csv',\
             'atlas-query-simpsons-season-20\Keyword.csv','atlas-query-simpsons-season-20\Vote.csv']
    
    df1,df2,df3,df4,df5,df6 = read_csv (paths)
    drop_tables (cur,rds_sql.drop_tables)
    #create_tables (cur,rds_sql.create_tables)
    #insert_into_tables (cur,rds_sql.insert_into_tables,df1,df2,df3,df4,df5,df6)

main()

#result = cur.fetchall()
#for row in result:
#    print (row)  
