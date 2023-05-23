from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def games_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from mytable"))

    games = []
    for row in result.all():
      games.append(dict(zip(result.keys(), row)))
    return games
