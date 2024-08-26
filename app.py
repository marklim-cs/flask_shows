import sqlite3
import os
from flask import Flask, g, render_template, request, jsonify
from flask_session import Session
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
DATABASE = os.getenv('DATABASE_URL')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # Allows us to treat rows as dictionaries
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    db = get_db()
    query  = "%" + request.args.get("q") + "%"
    if query:
        cursor = db.execute("SELECT * FROM shows WHERE title LIKE ?", (query,))
        rows = cursor.fetchall()
        # Converts each sqlite3.Row object into a standard Python dictionary
        shows = [dict(row) for row in rows]
    else:
        shows = []
    return jsonify(shows)