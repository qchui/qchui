import os


DEBUG=True

SECRET_KEY=os.urandom(24)

HOSTNAME='127.0.0.1'
PORT='3306'
DATABASE='qch'
USERNAME='root'
PASSWORD=''
DB_URI='mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,
                                                            PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI=DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS=False