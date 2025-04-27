from flask import Flask, render_template, request
from pymongo import MongoClient  # only if you're doing the backend too

app = Flask(__name__)

@app.route("/todo")
def todo_page():
    return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True)
