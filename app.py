from flask import Flask, render_template, request, redirect
from database import games_from_db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result",methods=['POST'])
def result():
  search = request.form['content']
  return render_template('result.html', search = search)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
