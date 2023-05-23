from flask import Flask, render_template, request
from database import games_from_db, games_name_from_db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result",methods=['POST'])
def result():
  games = games_from_db()
  games_name = games_name_from_db()
  search = request.form['content']
  correspondance = 0
  if search in games_name:
    correspondance = True
  else :
    correspondance = False
  return render_template('result.html', games=games, games_name=games_name,search=search, correspondance = correspondance)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
