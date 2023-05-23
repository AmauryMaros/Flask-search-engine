from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def games_name_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT Name FROM mytable2"))
    games_name = []
    for row in result.all():
      games_name.append(row[0])
      
    return games_name

def games_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM mytable2"))
    games = []
    for row in result.all() :
      games.append(dict(zip(result.keys(), row)))
      
    return games
